# Dockerfile
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the local project files to the Docker container
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install matplotlib numpy

# Make sure the output folder is accessible
RUN mkdir -p /app/output && chmod -R 777 /app/output

# Use CMD instead of ENTRYPOINT for easier shell access
CMD ["python3", "main.py"]
