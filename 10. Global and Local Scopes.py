spam = 42 # global variable

def eggs():
    spam = 42 # local variable

print ('Some code here.')
print ('Some more code.')

def spam():
    global eggs
    eggs = 'Hello'
    print(eggs)

eggs = 42
spam()
print(eggs)
