# for Loops
# Range Objects and List-Like Values
for i in range (4):
    print (i)

for i in [0, 1, 2, 3]:
    print (i)

# list function
print(list(range(4)))

print (list(range(0, 100, 2)))

# for i in range(len(someList))
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

supplies = ['pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])


# Multiple Assignment
cat = ['fat', 'orange', 'loud']
size = cat [0]
color = cat [1]
disposition = cat [2]
print (size)
print (color)
print (disposition)

size, color, disposition = 'skinny', 'black', 'quiet'
print(size, color, disposition)

# Swapping Variable
a = 'AAA'
b = 'BBB'
a,b = b,a
print (a)
print (b)

# Augmented Assignment Operators
spam = 42
spam = spam + 1
spam += 1
print(spam)
# spam +=1
# spam -=1
# spam *=1
# spam /=1
# spam %=1

