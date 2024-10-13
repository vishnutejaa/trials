import os
from email.message import EmailMessage
import smtplib
import ssl
import dotenv
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

email_sender = os.getenv('EMAIL_SENDER')
email_password= os.getenv('EMAIL_ENV_PASSWORD')# or from bash profile: os.environ.get('EMAIL_PASSWORD')
email_receiver = os.getenv('EMAIL_RECEIVER')


subject = 'This trial to send automated emails on python'
body = """
Hey, I have successfuly send an email using python
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)


context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

                        ## OR ##
#message = f'Subject: {subject}\n\n{body}'
# try:
#     with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
#         smtp.starttls()  # Secure the connection
#         smtp.login(email_sender, email_password)  # Use app-specific password here
#         smtp.sendmail(email_sender, email_receiver, message)
#         print('Email sent successfully.')
# except smtplib.SMTPAuthenticationError as e:
#     print(f'Error: {e}')



