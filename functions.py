import random

# To ger rid of duplicate code
def prompt(num):
    if num == 1:
        return 'it is what it is'
    elif num == 2:
        return 'it do be like that'
    elif num == 3: 
        return 'damn it has hands'
    else:
        return 'fk'
    
    # Every function ahs a return value, default is none

print(prompt(random.randint(1,5)))
listed = ['cat', 'dog', 'mouse']
print(listed, sep = 'AA')

print('cat', 'dog', 'mouse', sep = 'AA')