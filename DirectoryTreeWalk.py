# Walking a directory tree

import os
import shutil

# Returns three different values
for foldername, subfolders, filenames in os.walk(r'C:\Users\alex_\.vscode\Python\Automate the Boring Stuff\Automate_The_Boring_Stuff\folder'):
    print('The folder is ' + foldername)
    print('The subfolders in ' + foldername + ' are ' + str(subfolders))
    print('The filenames in ' + foldername + ' are ' + str(filenames))
    print()

    for subfolder in subfolders:
        if 'fish' in subfolders:
            #os.unlink(subfolder)
            print('rmdir on ' + subfolder)

    for file in filenames:
        if file.endswith('.txt'):
            #shutil.copy(os.join(foldername, file),  os.join(foldername, file + '.backup')
            print('create backup on ' + file)