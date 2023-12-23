# Start with Python 3.10 base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /usr/src/app

# Install the requests module
RUN pip install --no-cache-dir requests

# Copy the script.py file from your local plugin_scripts directory
# and rename it to app.py in the container
COPY plugin_scripts/script.py ./app.py

# Command to run when the container starts
CMD ["python", "./app.py"]

