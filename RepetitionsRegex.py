import re

message = 'The adventures of Batman'
batRegex = re.compile(r'Bat(wo)?man') # wo can appear 0 or 1 times
mo = batRegex.search(message)
print(mo.group())

message = 'The adventures of Batwoman'
mo = batRegex.search(message)
print(mo.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d') #? Means can appear 0 or 1 times
message = "My number is 416-546-9464, call me"
mo = phoneRegex.search(message)
print(mo.group())

# If no area code
message = "My number is 546-9464, call me"
mo = phoneRegex.search(message)
print(mo.group())

# * means matches 0 or more times

message = 'The adventures of Batwowowowowoman'
batRegex = re.compile(r'Bat(wo)*man') # wo can appear 0 or more times
mo = batRegex.search(message)
print(mo.group())

# + means 1 or more

message = 'The adventures of Batwowowowowoman'
batRegex = re.compile(r'Bat(wo)+man') # wo can appear 0 or more times
mo = batRegex.search(message)
print(mo.group())

# Adding +, ?, /
regex = re.compile(r'\+\?\*')
message = 'I learnt about +?* today'
mo = regex.search(message)
print(mo.group())

# To check exact repetitions, use{x}

# To check minimum and maximum reps, use{x,y}

# Greedy match, matches the longest maximum string

# Non greedy match, use{x,y}?, shortest string