print(list('Hello'))

name = 'Sophie'
print(name[1:3])

for letter in name:
    print(letter)

# Strings are immutable, cannot be modified in place
# varriables don't contain lists, contain reference to the list
# changes made to a list in a function will affect the list outside the function
# Can use \ for line breaks

def eggs(X):
    X.append('Hello')

spam = [1,2,3]
eggs(spam)
print(spam)