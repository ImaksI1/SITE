import smtplib, ssl, os

sender_gmail = "imaksand123i@gmail.com"
password = os.getenv("password")
receiver_gmail = "maksvijtovic98@gmail.com"
host = "smtp.gmail.com"
port = 465
context = ssl.create_default_context()
server = smtplib.SMTP_SSL(host, port, context=context)


def SendEmail(email):
    server.login(sender_gmail, password)
    server.sendmail(sender_gmail, receiver_gmail, email)


