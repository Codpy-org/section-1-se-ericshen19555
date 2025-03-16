# Use the official Python 3.11-slim image as base
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

COPY . .
# Install Flask
RUN pip install -r requirements.txt

# Copy all files from the current directory to /app in the container

# Run the Flask application
CMD ["python", "main.py"]
