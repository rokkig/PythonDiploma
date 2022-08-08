import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("email here with no @s", "password")
msg = "your message here"
server.sendmail("email with @", "receipient email with @", msg)
server.quit()

#only works for emails with no 2fa
