# Escape Charcters
print("That is Alice's cat.")

print('Say hi to Bob\'s mother.')

# \' Single quote
# \"" Double quote
# \t Tab
# \n Newline (line break)
# \\ Backlash

print('Hello there!\nHow are you?\nI\'m fine.')

# Raw Strings
print(r'Hello')

print(r'That is Carol\'s cat.') 

# Multiline Strings with Triple Quotes
print("""DEAr Alice, 
Eve's cat has ben arrested for catmapping, cat burglary,
and extortion.

Sincerely,
Bob.""") 

spam = """DEAr Alice, 
Eve's cat has ben arrested for catmapping, cat burglary,
and extortion.

Sincerely,
Bob."""

print(spam) 

# Similarities Between Strings and Lists
print('Hello World!')

spam = 'Hello World!'
print(spam[0])
print(spam[1:5])
print(spam[-1]) # Getting the last value
print('Hello' in spam)
print('x' in spam)
print('HELLO' in spam)


