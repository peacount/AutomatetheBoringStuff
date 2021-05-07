# Methods
spam = ['hello', 'hi', 'howdy', 'heyas']
# The index()List Method
print(spam.index('hello'))
print(spam.index('heyas'))
# print(spam.index('fskldjkjhflkshlkjhlfkjdhs'))

spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
print(spam.index('Pooka'))

# The append() and insert() List Methods
spam = ['cat', 'dog', 'bat']
spam.append('moose')
print(spam)

spam = ['cat', 'dog', 'bat']
spam.insert(1, 'chicken')
print(spam)
spam.append('moose')
spam.append('moose')
spam.append('moose')
spam.append('moose')
print(spam)

# spam = spam.append('moose') does not work, rather it will assign None to the whole spam list. 
# eggs = 'hello'
# eggs.append ('world') does not work, as the append function does not work for the string value. 

# The remove() List Method
spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')
print(spam)

# Compare with Delete funtion
spam = ['cat', 'bat', 'rat', 'elephant']
del spam[0]
print(spam)

spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
spam.remove('cat')
print(spam)

# The sort() List Method
spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam)

spam = ['ants', 'cats', 'dogs', 'badgers', 'elephant']
spam.sort()
print(spam)

spam.sort(reverse=True)
print(spam)

# "ASCII-betical" Order
spam = ['Alice', 'Bob', 'ants', 'Carol', 'cats']
spam.sort()
print(spam)

spam = ['a', 'z', 'A', 'Z']
spam.sort()
print(spam)

spam.sort(key=str.lower)
print(spam)

