# syntax=docker/dockerfile:1
FROM python:3.10-alpine

WORKDIR /code

# Environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Install build dependencies
RUN apk add --no-cache gcc musl-dev linux-headers

# Copy requirements and install Python packages
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the application code and monitoring script
COPY . .

# Install the requests library for the monitoring script
RUN pip install requests

# Copy the .env file
COPY .env .env

# Expose port
EXPOSE 5000

# Command to run the monitoring script and Flask app
CMD ["sh", "-c", "python monitor.py & flask run --debug"]



