spam = ['cat', 'bat', 'rat', 'elepahnt']
print (spam[0])

spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
print (spam [1] [4])

spam = ['cat', 'bat', 'rat', 'elepahnt']
print (spam[-1])
print (spam[-2])
print('The', spam[-1], 'is afraid of', spam[-3])


spam = [10, 20, 30]
spam[1] = 'Hello'
print(spam)

spam[1:3] = ['CAT', 'DOG', 'MOUSE']
print (spam)

spam = ['cat', 'bat', 'rat', 'elepahnt']
print (spam[:2])
print (spam[1:])

spam = ['cat', 'bat', 'rat', 'elepahnt']
del spam[2]
print(spam)
del spam[2]
print(spam)

print(len([1,2,3]))

print([1,2,3]+[4,5,6])
print('Hello'*3)
print([1,2,3]*3)

print(list('Hello'))

print('howdy' in ['hello', 'hi', 'howdy', 'heyas'])

print(42 in ['hello', 'hi', 'howdy', 'heyas'])

print('howdy' not in ['hello', 'hi', 'howdy', 'heyas'])