# Use the official Python 3.11-slim image as base
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install Flask
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files from the current directory to /app in the container
COPY . .

# Expose port 5000 to allow communication to/from the container
EXPOSE 5000

ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_POST=5000
ENV PYTHONUNBUFFERED=1

# Run the Flask application
CMD ["python", "main.py"]
