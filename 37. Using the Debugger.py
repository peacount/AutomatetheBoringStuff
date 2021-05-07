print('enter the first number of add:')
# first = input()
print('enter the second number of add:')
# second = input()
print('enter the third number of add:')
# third = input()
# print('the sum is '+ first + second + third)

# Stepping Into and Stepping Out
def blahBlahblahBlah():
    print('blah')
    print('blah')
    print('blah')
    moreBlah()
    print('blah')
    print('blah')
    print('blah')
    moreBlah()
    print('blah')
    print('blah')
    print('blah')
    print('blah')

def moreBlah():
    print('more blahs')
    print('more blahs')
    print('more blahs')

blahBlahblahBlah()

# breakpoints 
#! python3
import random

heads = 0

for i in range(1,1001):
    if random.randint(0,1) == 1:
        heads = heads+1
        if i==500:
            print ('Halfway done!')

print('Heads came up ' + str(heads) + 'times.')