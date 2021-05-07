# Various Ways to Work with String Values
print(list ('Hello'))

name = 'Zophie'
print(name[0])
print(name[1:3])
print(name[-2])

print('Zo' in name)
print('xxx' in name)

for letter in name:
    print(letter)

# Mutable and Immutalbe Data Types
name = 'Zophie the cat'
print(name[7])

# Creating New Strings from Slices
name = 'Zophie a cat'
newName = name[0:7] + 'the' + name [8:12]
print(newName)

# The difference between immutalbe and mutalbe comes up with "references"
# References
spam = 42
cheese = spam
spam = 100
print(spam)
print(cheese)

spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello!'
print (cheese)
print (spam)

# Immutable values don't hve this problem, because they can't be modified "in place". 
# They can only be replaced by new values. 

# Passing Lists in Function Calls
def eggs(cheese):
    cheese.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)

# The copy.deepcopy() Function
import copy

spam = ['A', 'B', 'C', 'D']
cheese = copy.deepcopy(spam)
cheese[1] = 42
print (cheese)
print(spam)

# Line Continuation
spam = ['apples',
        'orages',
        'bananas',
        'Cats']
print(spam)

print('Four score and seven ' + \
    'years ago')





