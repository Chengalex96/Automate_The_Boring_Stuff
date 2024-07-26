import re

beingsWithHelloRegex = re.compile(r'^Hello') 
# Must start with hello ^
print(beingsWithHelloRegex.search('Hi Hello there!'))

endsWithWorldRegex = re.compile(r'World!$') 
# $ sign at the end 
print(endsWithWorldRegex.search('Hi Hello there World!'))

# ^ + $ means the whole string must match
allDigitsRegex = re.compile(r'^\d+$')
print(allDigitsRegex.search('465465446465'))
print(allDigitsRegex.search('465465x446465'))

# . means any characters except newline

atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat'))

atRegex = re.compile(r'.{1,2}at')
print(atRegex.findall('The cat in the hat sat on the flat mat'))

# .* means any characters
# () Groups them and takes the greedy mode (longest string)

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall('First Name: Al Last Name: Chan'))

prime = 'Serve the public trust \n Protect innocent \n Uphold the law'

dotStar = re.compile(r'.*', re.DOTALL) # add case to include \n
print(dotStar.search(prime))