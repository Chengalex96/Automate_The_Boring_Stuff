# Files seperator

# Windows is \

import os
os.path.join('folder1', 'folder2', 'folder3')

print(os.sep) # Returns \ on windows

print(os.getcwd())

# Absolute file path (start with root folder) and relative file path
# . refers to this folder

print(os.path.abspath('MVO Constraints'))

print(os.path.relpath('MVO Constraints', 'c:\\Users\alex_'))

print(os.listdir(r'C:\Users\alex_\.vscode\Python\Automate the Boring Stuff\Automate_The_Boring_Stuff'))

print(os.path.getsize(r'C:\Users\alex_\.vscode\Python\Automate the Boring Stuff\Automate_The_Boring_Stuff\dict.py'))

# Find the total size of a folder

totalSize = 0

for filename in  os.listdir(r'C:\Users\alex_\.vscode\Python\Automate the Boring Stuff\Automate_The_Boring_Stuff'):
    if not os.path.isfile(os.path.join(r'C:\Users\alex_\.vscode\Python\Automate the Boring Stuff\Automate_The_Boring_Stuff', filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join(r'C:\Users\alex_\.vscode\Python\Automate the Boring Stuff\Automate_The_Boring_Stuff', filename))

print(totalSize)