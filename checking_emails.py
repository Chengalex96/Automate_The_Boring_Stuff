# Checking emails with Python

# IMAP: Internet Message Access Protocol

import imapclient
import pyzmail

conn = imapclient.IMAPClient('imap-mail.outlook.com', ssl=True) # Enter domain
email = 'theweebkage@hotmail.com'
password = 'Abcdkc001'

print(conn.login(email, password))

print(conn.select_folder("INBOX", readonly=True))

UIDs = conn.search(['FROM', email]) # String inside of a list, how to filter out which to search
print(UIDs) # list of emails that match 

rawMessage = conn.fetch([11118], "BODY[]") # Weird string of messages

print(rawMessage)

message = pyzmail.PyzMessage.factory(rawMessage[11118][b'BODY[]']) # Doesnt work for the promo email with alot of html links

print(message.get_subject())

print(message.get_addresses('from'))

print(message.get_addresses('to'))

print(message.get_addresses('bcc'))

print(message.text_part)

print(message.text_part.get_payload().decode('UTF-8'))

print(conn.list_folders())

# To delete emails

conn.select_folder('INBOX', readonly=False)
UIDs = conn.search(['FROM', email])
# conn.delete_messages(UIDs)