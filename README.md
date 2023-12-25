# PR Validation Buildkite Plugin

Validates your Github Pull Request properties(pr-title,etc) against a specification provided.

## Example

Add the following to your `pipeline.yml`:

```yml
steps:
  - plugins:
      - devdil/pr-validation#v1.0.5:
          pr-title:
           regex: "test"
           error_message: "your pr title adhere to <convention>"
    env:
       GITHUB_TOKEN: 'your_github_token_here'
          
```

## Configuration

### `pr-title.regex`

The regex used to validate your PR title

### `pr-title.error_message`
The error message to display if PR title validation fails.

## Developing

To run the tests:

```shell
docker-compose run --rm tests
```

## Contributing

1. Fork the repo
2. Make the changes
3. Run the tests
4. Commit and push your changes
5. Send a pull request