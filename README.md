# Web Server Monitoring

This project sets up a Dockerized Flask web application with a monitoring script to check its health periodically. If the web application is down or responds with a non-200 status code, or if it takes more than 10 seconds to respond, the monitoring service will send an email alert using the Namshi SMTP container.

## Prerequisites

- Docker and Docker Compose

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/sambender97/CorticoHealthTechTest.git
cd CorticoHealthTechTest
```
### Create and Configure the .env File
Create a .env file in the root directory of the project with the following contents:

```bash
EMAIL_FROM=your-email@gmail.com
EMAIL_TO=recipient-email@gmail.com
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-smtp-password
```
**In my email submission to Catherine Bartoline I have shared the required environment variables**

I created a new gmail account to use as the SMTP user for this test

### Build and Run the Containers
```bash
docker compose build
docker compose up
```
## Service Overview

This project sets up the following services:

- **web**: The Flask web application.
- **redis**: A Redis instance (used if required by your application).
- **monitor**: The monitoring script that checks the health of the Flask application.
- **smtp**: The SMTP server for sending email notifications.

## Code Structure

- **Dockerfile**: Builds the Docker image for the web service and monitoring script.
- **docker-compose.yml**: Defines and configures the services used in the application.
- **monitor.py**: Python script that monitors the web service and sends alerts if issues are detected.
- **.env**: Contains environment variables for email configuration.

## Important Choices and Considerations

- **Docker and Docker Compose**: Used for containerization to ensure consistency across different environments.
- **Namshi SMTP**: Chosen for its simplicity in setting up an SMTP server for sending emails.
- **Periodic Monitoring**: The script runs every 60 seconds to check the web service health and ensures timely notifications for potential issues.
- **Email Configuration**: Sensitive information is separated into a `.env` file to avoid hardcoding credentials in the source code.

## Assumptions

- **Network Configuration**: Assumes that the services can communicate with each other over the Docker network.
- **SMTP Credentials**: Assumes the user provides valid SMTP credentials and configuration in the `.env` file.

## Pros and Cons

**Pros**:

- **Modular Design**: Each component is contained within its own Docker container.
- **Automated Monitoring**: Automatically checks the health of the web application and alerts if issues are detected.

**Cons**:

- **Email Configuration**: Requires the user to provide email credentials, which might be sensitive.
- **Resource Usage**: Running multiple containers might consume more resources compared to a simpler setup.
