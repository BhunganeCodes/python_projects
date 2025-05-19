from email.message import EmailMessage
import ssl
import smtplib

email_sender = "thamsanqahadebe98@gmail.com"
email_password = "kfci tpfe mpdo sbek"

email_receiver = "siyandisbani@gmail.com"

subject = "This is Bhungane Codes"

body = """
This is Bhungane Codes' Python project called an email sender. I worked on this as part of my self-learning journey to learn how to utilize Python techniques on how to send my own emails.
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

