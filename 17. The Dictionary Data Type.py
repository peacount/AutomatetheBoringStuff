myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud' }
print(myCat['size'])
print ('My cat has ' + myCat['color'] + ' fur.')

# Dictionaries are unordered. 
eggs = {'name': 'Zohpie', 'species': 'cat', 'age':8}
ham = {'species': 'cat', 'name': 'Zophie', 'age': 8}
print (eggs == ham)

# Key Error
print ('name' in eggs)
print ('name' not in eggs)

# The keys(), values(), and items() Dictionary Methods
a=list(eggs.keys())
b=list(eggs.values())
c=list(eggs.items())
print(a)
print(b)
print(c)

for k in eggs.keys():
    print(k)

for v in eggs.values():
    print(v)    

for k, v in eggs.items():
    print (k,v)    

for i in eggs.items():
    print (i)

print(eggs)    

print('cat' in eggs.values())

# The get() Dictionary Method
if 'color' in eggs:
    print(eggs['color'])

print(eggs.get('age', 0))
print(eggs.get('color', ''))

picnicItems = {'apples':5, 'cups':2}
print ('I am brining ' +  str(picnicItems.get('napkins', 0)) + ' to the picnic.')

# The setdefault() Dictionary Method
eggs = {'name': 'Zohpie', 'species': 'cat', 'age':8}

if 'color' not in eggs:
    eggs['color'] = 'black'

eggs = {'name': 'Zohpie', 'species': 'cat', 'age':8}
eggs.setdefault('color', 'black')
print(eggs)

eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8 }
eggs.setdefault('color', 'black')
print (eggs)
eggs.setdefault('color', 'orange')
print (eggs)

# Character Counting Program Example
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character]+1

print(count)

# The pprint module
import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character]+1

pprint.pprint(count)

rjtext = pprint.pformat(count)
print(rjtext)




