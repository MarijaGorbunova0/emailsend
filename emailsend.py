import smtplib, ssl
from email.message import EmailMessage
smtp_server = "smtp.gmail.com"
port = 587
sender_email = "mariarapirovna@gmail.com"
#to_email = "mariarapirova@gmail.com"
password = input("Type your password(copied gmail) ")
#create a secure SSL conntex
context = ssl.create_default_context()
msg = EmailMessage()
msg.set_content("оо")
msg["Subject"] = "Tere Roman"
msg["From"] = "mariarapirovna@gmail.com"
msg["To"] = "sandakovroman2@gmail.com"
#"try to log to server and email
try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo() #can be omitted
    server.starttls(context = context)
    server.ehlo()
    server.login(sender_email, password)
    #server.sendmail(sender_email, msg)
    server.send_message(msg)
except Exception as Viga:
    print(Viga)
finally:
    server.quit()


