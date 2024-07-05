import smtplib, ssl

sender_gmail = "imaksand123i@gmail.com"
password = "rxvevqgjdnqptmch"
receiver_gmail = "maksvijtovic98@gmail.com"
host = "smtp.gmail.com"
port = 465
context = ssl.create_default_context()
server = smtplib.SMTP_SSL(host, port, context=context)


def SendEmail(message):
    server.login(sender_gmail, password)
    server.sendmail(sender_gmail, receiver_gmail, message)


