import os
import sys
import requests

#print env vars....
for name, value in os.environ.items():
    print("{0}: {1}".format(name, value))

"""
Validates pr title against a specifiction specifiied in the configuration
provided by the user in plugin definition
"""
def validate_pr_title(pr_number, github_token):
    BUILDKITE_REPO = os.environ.get('BUILDKITE_REPO')
    if not BUILDKITE_REPO:
        print('variable not set, ensure the buildkite environment variable BUILDKITE_REPO is set')
        sys.exit(1)
    repo_name = BUILDKITE_REPO.split('.com')[1].split('.git')[0][1:]
    domain_name = "github.com"

    # GitHub API URL for the pull request
    url = f"https://api.{domain_name}/repos/{repo_name}/pulls/{pr_number}"

    # Set up headers for authentication (if a token is provided)
    headers = {}
    if github_token:
        headers["Authorization"] = f"token {github_token}"

    # Make the request
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        pr_data = response.json()
        pr_title = pr_data["title"]
        print(f"Title of Pull Request #{pr_number}: {pr_title}")
    else:
        print(f"Failed to fetch data: {response.status_code} - {response.reason}")
        sys.exit(1)


GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
if not GITHUB_TOKEN:
    print('GitHub Token is required to proceed! Please pass a valid github TOKEN')
    sys.exit(1)

PR_TITLE_REGEX = os.environ.get('PR-TITLE')
PR_NUMBER = os.environ.get('BUILDKITE_PULL_REQUEST')
if not PR_TITLE_REGEX or not PR_NUMBER:
    print('Should be a pull request to validate. Please ensure this step is only executed for a pull request.')
    sys.exit(1)
else:
    validate_pr_title(PR_NUMBER, GITHUB_TOKEN)
