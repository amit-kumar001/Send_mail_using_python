import smtplib
e_user='SENDER MAIL_ID'
e_send='RECEIVER MAIL_ID'

# creates SMTP session

s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login(e_user, "Password")

# message to be sent
message = "I'm too excited and sir make me calm"

# sending the mail
s.sendmail(e_user, e_send, message)

# terminating the session
s.quit()
