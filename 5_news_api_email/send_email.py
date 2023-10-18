import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to, subject, message):
    gmail_address = None #to_fill
    gmail_password = None #to_fill

    # Gmail's SMTP server details
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # Port for TLS encryption

    msg = MIMEMultipart()

    # Set the sender's email address and recipient's email address
    msg['From'] = gmail_address
    msg['To'] = to  # Replace with the recipient's email address
    msg['Subject'] = subject


    msg.attach(MIMEText(message, 'plain'))

    try:
        # Create an SMTP object and connect to Gmail's SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)

        # Start TLS encryption (secure connection)
        server.starttls()

        # Log in to your Gmail account
        server.login(gmail_address, gmail_password)

        # Send the email
        server.sendmail(gmail_address, to, msg.as_string())

        # Close the connection
        server.quit()
        print('Email sent successfully!')
    except Exception as e:
        print(f'An error occurred: {str(e)}')