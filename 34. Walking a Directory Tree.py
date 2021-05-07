# The os.walk() function
import os, shutil
for folderName, subfolders, filenames in os.walk('c:\\delicious_backup'):
    print('The folder is '+ folderName)
    print('The subhodlers in ' + folderName + ' are: ' + str(subfolders))
    print('The filenames in ' + folderName + ' are: ' + str(filenames))
    print()

    for subholder in subfolders:
        if 'fish' in subfolders:
            # os.rmdir(subholders)
            print('rmdir on ' + subholders)
    
    for file in filenames:
        if file.endswith('.py'):
            # shutil.copy(os.join(folderName, file), os.join(folderName, file) + '.backup')