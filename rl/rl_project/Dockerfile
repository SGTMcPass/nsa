# Use the official Python image from DockerHub
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the local project files to the Docker container
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Set the entrypoint for the container to run the main.py script
ENTRYPOINT ["python", "main.py"]
