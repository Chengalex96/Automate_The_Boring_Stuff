import re  

message = 'Call me at 415-555-2048 or at 415-562-5165'

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')# regular expression

# Groups aer created in RegEx with ()

MatchedObject = phoneNumRegex.search(message)

print(MatchedObject.group()) # Returns full matching string
print(MatchedObject.group(1)) # Group for area code, first group
print(MatchedObject.group(2))

# If the area code has (416)
phoneNumRegex = re.compile(r'\(\d\d\d\) (\d\d\d-\d\d\d\d)')# regular expression to include the () inside area code
message = 'Call me at (415) 555-2048 or at (415) 562-5165'

MatchedObject = phoneNumRegex.search(message)

print(MatchedObject.group())

# Using Pipes (|) to match one of many groups
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
message = 'Batmobile lost a wheel'
mo = batRegex.search(message)
print(mo.group())
print(mo.group(1)) # group number