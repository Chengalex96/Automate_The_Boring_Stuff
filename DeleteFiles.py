import os

# Deletes a single folder
# os.unlink('spam2.txt')

# Remove empty directory
# os.rmdir(r'C:\Users\alex_\.vscode\Python\Automate the Boring Stuff\Automate_The_Boring_Stuff\folder')

import shutil
# Removes folder and all the contents
# shutil.rmtree(r'C:\Users\alex_\.vscode\Python\Automate the Boring Stuff\Automate_The_Boring_Stuff\folder')


import os
for filename in os.listdir():
    if filename.endswith('.txt'):
        #os.unlink(filename) # Dry run
        print(filename)

# Sends to recycling bin instead
import send2trash
send2trash.send2trash('hello2.txt')