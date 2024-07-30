import re

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall('Agent Alice gave the paper to Agent Bob.'))

# Find and substitute WITH REDACTED

print(namesRegex.sub('REDACTED', 'Agent Alice gave the paper to Agent Bob.'))

# Find and substitute with Agent and the first letter

namesRegex = re.compile(r'Agent (\w)\w*')

print(namesRegex.findall('Agent Alice gave the paper to Agent Bob.'))

print(namesRegex.sub(r'Agent \1****', 'Agent Alice gave the paper to Agent Bob.'))
# \1 refers to the group

# Verbose format, add documentation to complicated code by formatting and comments and spaces
re.compile(r'''
           \d\d\d # Area code
           -    #First Dash
           \d\d\d # First 3 digits
           - # Second dash
           \d\d\d\d # last 4 digits''', re.VERBOSE | re.IGNORECASE | re.DOTALL) # Can pass by multiple arguments