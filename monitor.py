import smtplib
import requests
import time
import os
from email.mime.text import MIMEText

# Load environment variables
EMAIL_FROM = os.getenv('EMAIL_FROM')
EMAIL_TO = os.getenv('EMAIL_TO')
SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = int(os.getenv('SMTP_PORT'))
SMTP_USER = os.getenv('SMTP_USER')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')

URL = "http://web:5000/"
TIMEOUT = 10  # seconds
SUBJECT = "Service Down Alert"

def send_email(subject, message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO
    
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
            print(f"INFO: Email sent to {EMAIL_TO}")
    except Exception as e:
        print(f"ERROR: Failed to send email. Exception: {e}")

def log_message(message):
    print(message)

def monitor():
    while True:
        start_time = time.time()
        try:
            response = requests.get(URL, timeout=TIMEOUT)
            elapsed_time = time.time() - start_time
            if response.status_code != 200:
                log_message(f"ERROR: Received status code {response.status_code}. Response time: {elapsed_time:.2f}s")
                send_email(SUBJECT, f"Received status code {response.status_code} from {URL}. Response time: {elapsed_time:.2f}s")
            elif elapsed_time > TIMEOUT:
                log_message(f"WARNING: Response took too long: {elapsed_time:.2f}s")
                send_email(SUBJECT, f"Response took too long from {URL}: {elapsed_time:.2f}s")
            else:
                log_message(f"INFO: Endpoint is healthy. Response time: {elapsed_time:.2f}s")
        except requests.exceptions.RequestException as e:
            elapsed_time = time.time() - start_time
            log_message(f"ERROR: Exception occurred: {e}. Response time: {elapsed_time:.2f}s")
            send_email(SUBJECT, f"Exception occurred: {e}. Response time: {elapsed_time:.2f}s")

        time.sleep(60)  # Wait for 60 seconds before the next check

if __name__ == "__main__":
    time.sleep(60)  # Wait for 60 seconds before the first check to give time for initialization
    monitor()
