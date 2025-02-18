# Use Python base image
FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY . /app

# Install Flask
RUN pip install flask

# Expose port 5000 to the host machine
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]
