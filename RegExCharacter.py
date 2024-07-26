import re
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
message = "Cell: 416-555-2165 and Home: 415-555-1312 "

print(phoneRegex.findall(message)) # Returns a list if there are 0 or 1 groups

phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
message = "Cell: 416-555-2165 and Home: 415-555-1312"
print(phoneRegex.findall(message)) # Returns a list of touples

digitRegex = re.compile(r'(0|1|2|3|4|5|6|7|8|9)') # Same as \d
# \D is any character that is not a numeric digit from 0 to 0
# \w is any letter, digit or underscore
# \W is the opposite 
# \s is any space, tab, or newline character, \S is the opposite

lyrics = '''12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing,
    8 maids a milking, 7 swans a swimming, 6 gessae a laying, 5 golden rings, 4 calling birds, 3 french hens,
    2 turtle dopves, and 1 partridge in a pear tree'''

xmasRegex = re.compile(r'\d+\s\w+') # any digit + single space + 1 or more words, only goes to the first word since there's a space after
print(xmasRegex.findall(lyrics))

vowelRegex = re.compile(r'[aeiouAEIOU]{2}') # Same as r'[a|e|i|o|u], can also do ranges like [a-f] # picks out vowels
print(vowelRegex.findall(lyrics))

# Negative Character Class, do the opposite
vowelRegex = re.compile(r'[^aeiouAEIOU]{2}') # Same as r'[a|e|i|o|u], can also do ranges like [a-f] # picks out anyhting that is not in the bracket
print(vowelRegex.findall(lyrics))