import shutil

shutil.copy('hello.txt', 'spam.txt')

# rename by moving to the same folder with a different name
shutil.move('spam.txt', 'spam2.txt')

# shutil.copytree # Copys the folder