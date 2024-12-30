import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        # Create message container
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()

        print("Email sent successfully!")

    except Exception as e:
        print(f"Error: {e}")

# Usage
if __name__ == "__main__":
    sender_email = "joshuaosemeke60@gmail.com"
    sender_password = "Cyb3r3nc3Pa55word1%"
    recipient_email = "semekjoshua@gmail.com"
    subject = "Test Email"
    body = "Hello, this is a test email sent from Python!"

    send_email(sender_email, sender_password, recipient_email, subject, body)
