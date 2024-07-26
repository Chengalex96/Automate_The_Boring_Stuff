def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False # No area code
    if text[3] != '-':
        return False #Missing dash
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False # No first three digits
    if text[7] != '-':
        return False #Missing dash
    for i in range(8, 11):
        if not text[i].isdecimal():
            return False # last 4 digits
    return True

num = '416-555-1234'
num = 'hi'

print(isPhoneNumber(num))

message = 'Call me at 415-555-2048 or at 415-562-5165'
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone Number found: ' + chunk)
        foundNumber = True
if not foundNumber:
    print('No phone numbers')

# Imported expressions - alot less code

import re

message = 'Call me at 415-555-2048 or at 415-562-5165'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # regular expression
# Uses raw strings
MatchedObject = phoneNumRegex.search(message)
print(MatchedObject.group()) # group message to find matching text
MatchedObject = phoneNumRegex.findall(message)
print(MatchedObject)
