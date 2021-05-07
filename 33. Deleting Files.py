import os
# os.unlink(): deletes a single file
# print(os.getcwd())
# os.unlink('bacon.txt')

# os.rmdir(): Delete an empty folder. 
# os.rmdir('c:\\delicious')

# shutil.rmtree(): deletes a folder and its entire contents
# import shutil
# shutil.rmtree('c:\\delicious')

# Dry Run
import os

os.chdir('C:\\Users\\jenny\\MyPythonScripts')

for filename in os.listdir():
    if filename.endswith('.txt'):
        # os.unlink(filename)
        print(filename)

# The send2trash Module
import send2trash
send2trash.send2trash('C:\\Users\\jenny\\MyPythonScripts\\hello2.txt')