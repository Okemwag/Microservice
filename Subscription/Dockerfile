# Use the official Python image from the Docker Hub
FROM python:3-slim

# Expose the application port
EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pipenv
RUN pip install pipenv

# Set work directory
WORKDIR /app

# Copy Pipfile and Pipfile.lock to the working directory
COPY Pipfile Pipfile.lock /app/

# Install dependencies using pipenv
RUN pipenv install --deploy --ignore-pipfile

# Copy the application code
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["pipenv", "run", "gunicorn", "--bind", "0.0.0.0:8000", "subscription.wsgi"]
