helloFile = open(r'C:\Users\alex_\.vscode\Python\Automate the Boring Stuff\Automate_The_Boring_Stuff\hello.txt')
content = helloFile.read()
print(content)

# Ctrl + Y to redo

helloFile = open(r'C:\Users\alex_\.vscode\Python\Automate the Boring Stuff\Automate_The_Boring_Stuff\hello2.txt', 'w')
helloFile.write('Heya!')
helloFile.write('Heya!')
helloFile.write('Heya!')

helloFile = open(r'C:\Users\alex_\.vscode\Python\Automate the Boring Stuff\Automate_The_Boring_Stuff\hello.txt', 'a')
helloFile.write('Hellllllo')

import os
print(os.getcwd())

import shelve
shelfFile = shelve.open('mydata')
shelfFile ['cats'] = ['Zophie', 'Pooka', 'Mimmie']

shelfFile = shelve.open('mydata')
print(shelfFile['cats'])

# Stores in 3 binary file data, similar to dictionaries

print(list(shelfFile.keys()))
print(list(shelfFile.values()))