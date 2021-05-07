# os.path.join()
import os
print(os.path.join ('folder1', 'folder2', 'folder3', 'file.png'))
print(os.sep)

# os.getcwd(): current working directory
print(os.getcwd())

# os.chdir(): change directory
os.chdir('c:\\')
print(os.getcwd)

# Absolute and Relative Paths
'c:\folder1\folder2\spam.png'  # Absolute Paths
'\folder2\spam.png'  # Relative Paths

# The . (this folder) and .. (parent folder) Folders


os.chdir('c:\\Users\\jenny\\OneDrive\\Documents\\Prof Development\\Python\\Automate the Boring Stuff')
# os.path.abspath() and os.path.isabs()
print(os.path.abspath('spam.png'))

print(os.path.abspath('..\\..\\spam.png'))

print(os.path.isabs('..\\..\\spam.png')) # results in False
print(os.path.isabs('c:\\folder\\folder')) # reults in True

# os.path.relpath()
print(os.path.relpath('c:\\folder1\\folder2\\spam.png', 'c:\\folder1'))

# os.path.dirname(), os.path.basename()
print(os.path.dirname('c:\\folder1\\folder2\\spam.png'))
print(os.path.basename('c:\\folder1\\folder2\\spam.png'))
print(os.path.basename('c:\\folder1\\folder2'))

# os.path.exists
print(os.path.exists('c:\\folder1\\folder2\\spam.png'))
print(os.path.exists('c:\\windows\\system32\\calc.exe'))

# os.path.isfile(), os.pathisdir()
print(os.path.isfile('c:\\windows\\system32\\calc.exe'))
print(os.path.isfile('c:\\windows\\system32'))

print(os.path.isdir('c:\\windows\\system32\\calc.exe'))
print(os.path.isdir('c:\\windows\\system32'))

# os.path.getsize(), os.listdir()
print(os.path.getsize('c:\\Users\\jenny\\OneDrive\\Documents\\Prof Development\\Python\\Automate the Boring Stuff'))
print(os.listdir('c:\\Users\\jenny\\OneDrive\\Documents\\Prof Development\\Python\\Automate the Boring Stuff'))

# Example Code: Finding the total size of all files in a folder
totalSize = 0
for filename in os.listdir('c:\\Users\\jenny\\OneDrive\\Documents\\Prof Development\\Python\\Automate the Boring Stuff'):
    if not os.path.isfile(os.path.join('c:\\Users\\jenny\\OneDrive\\Documents\\Prof Development\\Python\\Automate the Boring Stuff', filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join('c:\\Users\\jenny\\OneDrive\\Documents\\Prof Development\\Python\\Automate the Boring Stuff', filename))

print(totalSize)

# os.makedirs()
os.makedirs('c:\\delicious\\walnut\\waffles')

os.path.isdir('c:\\users\\jenny\\anaconda3\\lib\\site-packages')

