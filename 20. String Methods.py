# upper(), lower()
spam = 'Hello world!'
spam.upper()
print(spam.lower()) 

#isupper(), islower()
spam = 'Hello world!'
print(spam.islower())

spam = 'hello world!'
print(spam.islower())

spam = 'HELLO WORLD!'
print(spam.isupper())

spam = ''
spam.isupper()
print(spam.islower())

print('12345'.islower())

print('Hello'.upper())

print('Hello'.upper().isupper())

# isalpha() - letters only
# isalnum() - letters and number only
# isdecimal() - numbers only
# isspace() - whitespace only
# istitle() - titlecase only

print('hello'.isalpha())

print('hello123'.isalpha())

print('hello123'.isalnum())

print('123'.isdecimal())

print('     '.isspace())

print('Hello world!'[5].isspace())

print('This Is Title Case'.istitle())

print('Hello world!'.title())

# starts with(), ends with()
print('Hello world!'.startswith('Hello'))

print('Hello world!'.startswith('H'))

print('Hello world!'.startswith('ello'))

print('Hello world!'.endswith('world!'))

print('Hello world!'.endswith('world'))

# join()
print(','.join(['cats', 'rats','bats']))
print(''.join(['cats', 'rats','bats']))
print(' '.join(['cats', 'rats','bats']))
print('\n\n'.join(['cats', 'rats','bats']))

# split()
print('My name is Simon'.split())
print('My name is Simon'.split('m'))

# ljust(), rjust()
print('Hello'.rjust(10))
print(len('     Hello'))
print('Hello'.ljust(10))
print('Hello'.ljust(20))
print('Hello'.ljust(20, '*'))
print('Hello'.ljust(25, '-'))

# center()
print('Hello'.center(20))
print('Hello'.center(20, '='))

name ='Al'
print(name.center(20, '='))

# strip(), rstrip(), lstrip()
print('Hello'.rjust(10))

spam = 'Hello'.rjust(10)
print(spam.strip())
print(spam)
spam = spam.strip()
print(spam)

print('    x   '.strip())
print('    x   '.lstrip())
print('    x   '.rstrip())

print('SpamSpamBAconSpamEggsSpamSpam'.strip('ampS'))

spam = 'Hello there!'
print(spam.replace('e', 'xyz'))

# The pyperclip Module

