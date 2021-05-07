# A Non-Regular Expression Example
def isPhoneNumber(text): # 415-555-1011
    if len(text) != 12:
        return False # not phone number-sized
    for i in range (0,3):
        if not text[i].isdecimal():
            return False # no area code
    if text[3] != '-':
        return False # missing dash
    for i in range (4,7):
        if not text[i].isdecimal():
            return False # no first 3 digits
    if text [7] != '-':
        return False # no first 3 digits
    for i in range (8,12):
        if not text[i].isdecimal():
            return False # missing last 4 digits
    return True

print (isPhoneNumber('415-555-1234'))

print (isPhoneNumber('hello'))

message = 'Call me 415-555-1011 tomorrow, or at 415-555-9990 for my office'
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: '+ chunk)
        foundNumber = True
    if not foundNumber:
        print('Could not find any phone numbers.')

# The re Module
import re

message = 'Call me 415-555-1011 tomorrow, or at 415-555-9990 for my office'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # call the re.complie() function to create a match object. 
mo = phoneNumRegex.search(message) # call the regex object's search() method to create a match object. 
print(mo.group()) # call the match object's group() method to get the matched string. 

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # \d is the regex for a numeric digit character. 
mo = phoneNumRegex.search('Call me 415-555-1011 tomorrow, or at 415-555-9990 for my office')
print(mo.group()) # 

# The findall() Method
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') 
mo = phoneNumRegex.findall('Call me 415-555-1011 tomorrow, or at 415-555-9990 for my office') 
print(mo)

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumRegex.findall('Call me 415-555-1011 tomorrow, or at 415-555-9990 for my office'))

