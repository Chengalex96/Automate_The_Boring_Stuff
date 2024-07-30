# ToDo comments

import re
import pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile(r'''
           # 415-555-5000, 555-0000, (415) 555-5555, 555-0000 ext 1234, ext. 1234, x12345
        (
           ((\d\d\d)|(\(\d\d\d\)))? # area code (optional), area code with or without bracket, also optional with the ?
           (\s|-) # first seperator
           \d\d\d # first 3 digits
           - # seperator
           \d\d\d\d # last 4 digits
           (((ext(\.)?\s) |x) # extension (optional) word part
           (\d{2,5}))?# extension (optional) number part
        )
           ''', re.VERBOSE)

# Create Regex for emails
emailRegex = re.compile(r'''
                        #some.+_thing@something.com

                        [a-zA-Z0-9_.+]+ # name part, make our own character class
                        @ # @ symbol
                        [a-zA-Z0-9_.+]+ # domain name part
                        ''', re.VERBOSE)

# Get text off clipboard
text = pyperclip.paste()

# Extract email/phone from text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNum = []
for phoneNumber in extractedPhone:
    allPhoneNum.append(phoneNumber[0])

# print(extractedPhone)
print(allPhoneNum)
print(extractedEmail)

# Copy email/phone to clipboard
results = '\n'.join(allPhoneNum) + '\n'.join(extractedEmail)
print(results)

pyperclip.copy(results)