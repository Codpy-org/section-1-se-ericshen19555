# Use the official Python 3.11-slim image as base
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install Flask
RUN pip install flask

# Copy all files from the current directory to /app in the container
COPY . /app

# Expose port 5000 to allow communication to/from the container
EXPOSE 5000

# Run the Flask application
CMD ["python", "main.py"]
