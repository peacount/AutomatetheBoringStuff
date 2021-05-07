import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumRegex.search('My number is 415-555-4242')
mo = phoneNumRegex.search ('My number is 415-555-4242')
print(mo.group())

# Groups
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search ('My number is 415-555-4242')
print(mo.group())
print(mo.group(1))
print(mo.group(2))

phoneNumRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo = phoneNumRegex.search ('My number is 415-555-4242')
mo = phoneNumRegex.search ('My number is (415) 555-4242')

# | Pipe Character
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group()) # calling group() or group(0) returns the full matching string

# mo = batRegex.search('Batmotorcycle lost a wheel')
# print(mo.group())

mo = batRegex.search('Batmobile lost a wheel')
print(mo.group(1)) # calling group(1) returns group 1