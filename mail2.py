# Python code to illustrate Sending mail from
# your Gmail account
import smtplib
e_user='provide mail id from you want to send mail'
e_send='provide mail id which you want to send mail'

# creates SMTP session

s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login(e_user, "Password")

# message to be sent
message = "i'm too excited and sir make me calm"

# sending the mail
s.sendmail(e_user, e_send, message)

# terminating the session
s.quit()
