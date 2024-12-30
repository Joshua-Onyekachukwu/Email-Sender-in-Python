import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['From'] = 'Joshua Onyekachukwu'
email['To'] = 'semekjoshua@Gmail.com'
email['Subject'] = 'You have won 1,000,000 dollars in your email'

email.set_content(html.substitute({'name': 'Joshua'}), 'html')


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.starttls()
    smtp.login(user='zerotomastery1@gmail.com', password='helloztmmyoldfriend1')
    smtp.send_message(email)
    smtp.close()
    print('Email sent!')
