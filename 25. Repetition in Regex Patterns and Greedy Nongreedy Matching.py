import re
# ? (zero or one)
batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group())

mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())

mo = batRegex.search('The Adventures of Batwowowowoman')
print(mo)

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 415-555-1234. Call me tomorrow')
print(mo.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 555-1234. Call me tomorrow')
print(mo.group())

# For example, if you wanted a regex object for the text "dinner?" (with the question mark),
# you would call:
# re.compile(r'dinner\?') Note the slash in \?
# In the above case, "dinner" is not optional, we are literally looking for a question mark: "dinner?"

# * (zero or more)
batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The Adventure of Batman')
print(mo.group())

mo = batRegex.search('The Adventure of Batwoman')
print(mo.group())

mo = batRegex.search('The Adventure of Batwowowowoman')
print(mo.group())

# + (one or more)
batRegex = re.compile(r'Bat(wo)+man')
#mo = batRegex.search('The Adventure of Batman')
#print(mo.group())

mo = batRegex.search('The Adventure of Batwoman')
print(mo.group())

mo = batRegex.search('The Adventure of Batwowowowoman')
print(mo.group())

# Escaping ?, * and +
regex = re.compile(r'\+\*\?')
mo = regex.search('I learned about +*? regex syntax')
print(mo.group())

regex = re.compile(r'(\+\*\?)+')
mo = regex.search('I learned about +*?+*?+*?+*?+*? regex syntax')
print(mo.group())

# {x} exactly x
haRegex = re.compile(r'(Ha){3}')
mo = haRegex.search('He said "HaHaHa"')
print(mo.group())

phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
mo = phoneRegex.search('My numbers are 415-555-1234,555-4242,212-555-0000')
print(mo)
print(mo.group())

# {x,y} at least x, at most y
haRegex = re.compile(r'(Ha){3,5}')
mo = haRegex.search('He said "HaHaHa"')
print(mo.group())

mo = haRegex.search('He said "HaHaHaHaHa"')
print(mo.group())

haRegex = re.compile(r'(Ha){,5}')
mo = haRegex.search('He said "HaHaHa"')
print(mo.group())

haRegex = re.compile(r'(Ha){3,}')
mo = haRegex.search('He said "HaHaHa"')
print(mo.group())

# Greedy Match
digitRegex = re.compile(r'(\d){3,5}')
print(digitRegex.search('1234567890'))
mo = digitRegex.search('1234567890')
print (mo)
print(mo.group())

# Non-Greedy Match
digitRegex = re.compile(r'(\d){3,5}?')
print(digitRegex.search('1234567890'))
mo = digitRegex.search('1234567890')
print (mo)
print(mo.group())

