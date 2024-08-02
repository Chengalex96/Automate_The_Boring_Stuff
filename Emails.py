# Emails for Notifications

# SMTP: Simple Mail Transfer Protocol

import smtplib

conn = smtplib.SMTP('smtp-mail.outlook.com', 587) # Create a conenction, with domain name and port number
# Outlook is smtp-mail.outlook.com

print(type(conn))

print(conn)

print(conn.ehlo()) #to connect

print(conn.starttls()) # for encryption

email = '@hotmail.com'
password = 'password'

print(conn.login(email, password)) # credentials

conn.sendmail(email, email, 'Subject: XXXXXX \n\n So long \n\n Alex') # send mail, subject and body

conn.quit()

# There's a limit of output mails (~ 100)