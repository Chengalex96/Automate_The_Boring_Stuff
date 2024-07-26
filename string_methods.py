# Returns a new string since they're immutable

spam = 'Hello World!'

print(spam.lower())
print(spam.upper())

# Good for inputs
# Can also check using isupper() or islower() for bool
# If it has 1 upper case, then islower is false

print(spam.isupper())
print(spam.islower())
print(spam.isalpha())
print(spam.isalnum())
print(spam.isdecimal())
print(spam.isspace())
print(spam.istitle()) # Each word is capitalized

print(spam.startswith('Hello'))
print(spam.endswith('orld!'))

print(','.join(['cat', 'bat', 'hat']))
print('\n\n'.join(['cat', 'bat', 'hat']))

print(spam.split('l'))

#'ljust and rjust to add white space padding
print(spam.rjust(20,'*'))
print(spam.center(20,'*'))

# Use spam.strip() to remove white space
print(spam.replace('e', 'XYZ'))

import pyperclip
pyperclip.copy(spam)
# Check: Hello World!, copies to clipboard