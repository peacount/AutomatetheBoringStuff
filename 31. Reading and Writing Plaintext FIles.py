# Plaintext and Binary Files

# The open() Function
open('C:\\Users\\jenny\\MyPythonScripts\\hello.txt')

# Read Mode
helloFile = open('C:\\Users\\jenny\\MyPythonScripts\\hello.txt')
helloFile.read()
helloFile.close()

helloFile = open('C:\\Users\\jenny\\MyPythonScripts\\hello.txt')
content = helloFile.read()
print(content)
helloFile.close()

# Readline Method
helloFile = open('C:\\Users\\jenny\\MyPythonScripts\\hello.txt')
content = helloFile.readlines()
print(content)
helloFile.close()

# Write Mode
helloFile = open('C:\\Users\\jenny\\MyPythonScripts\\hello2.txt', 'w')
helloFile.write('Hello!!!!!\n')
helloFile.write('Hello!!!!!\n')
helloFile.write('Hello!!!!!')
helloFile.close()

helloFile = open('C:\\Users\\jenny\\MyPythonScripts\\hello2.txt')
content = helloFile.read()
print(content)
helloFile.close()

baconFile = open('bacon.txt', 'w')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()

import os
print(os.getcwd())

baconFile = open('bacon.txt', 'a')
baconFile.write('\n\nBacon is delicious.')
baconFile.close()

baconFile = open ('bacon.txt')
content = baconFile.read()
print(content)

# Append Mode
helloFile = open('C:\\Users\\jenny\\MyPythonScripts\\hello.txt', 'a')

# The Shelve Module
import shelve
# The shelve.open() Method
shelfFile = shelve.open('mydata')
shelfFile['cats']= ['Zophie', 'Pooka', 'Simon', 'Fat-tail', 'Cleo']
shelfFile.close()

shelfFile = shelve.open('mydata')
print(shelfFile['cats'])
shelfFile.close()

# The keys() and values() Shelf Methods
shelfFile = shelve.open('mydata')
print(shelfFile.keys())
print(list(shelfFile.keys()))
print(list(shelfFile.values()))

