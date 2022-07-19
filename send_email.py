# from email import message
# import re
import smtplib
import ssl
from email.message import EmailMessage

from django.dispatch import receiver
from regex import E

subject = "Email from Python"
body = "hello! I'm a Python BOT, Hope you're doing well!"
sender_email = "shaileshgaddam22@gmail.com"
receiver_email = "shaileshgaddam117@gmail.com"

password  = input("Enter a Password : ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)

context = ssl.create_default_context()
print("Sending Mail....")

with smtplib.SMTP_SSL("smtp.gmail.com", 465 , context=context) as server:
    server.login(sender_email , password)
    server.sendmail(sender_email, receiver_email ,message.as_string())
print("mail send successfully!")