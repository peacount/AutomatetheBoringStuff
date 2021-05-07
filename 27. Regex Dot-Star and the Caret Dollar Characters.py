import re

# ^ MEANS THE STRING MUST START WITH THE PATTERN
beginsWithHelloRegex = re.compile(r'^Hello')
mo = beginsWithHelloRegex.search('Hello there!')
print(mo.group())

mo = beginsWithHelloRegex.search('He said "Hello!"')
print(mo)

# $ MEANS THE STRING MUST ENDS WITH THE PATTERN
endsWithWorldRegex = re.compile(r'world!$')
mo = endsWithWorldRegex.search('Hello world!')
print(mo.group())

mo = endsWithWorldRegex.search('Hello world!srhgielsknxitleidu')
print(mo)

# ^both$ means pattern must match the entire string. 
allDigitsRegex = re.compile(r'^\d+$')
mo = allDigitsRegex.search('2637459604893746')
print(mo.group())

mo = allDigitsRegex.search('2637459x604893746')
print(mo)

# . (anything except newline)
atRegex = re.compile(r'.at')
mo = atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo)

atRegex = re.compile(r'.{1,2}at')
mo = atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo)

# Dot-Star to Match Anything
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.findall('First Name: Al Last Name: Sweigart')
print(mo)

# (.*) is greedy
# (.*?) is non-greedy
serve = '<To serve humans> for dinner.>'
nongreedy = re.compile(r'<(.*?)>')
mo = nongreedy.findall(serve)
print(mo)

serve = '<To serve humans> for dinner.>'
greedy = re.compile(r'<(.*)>')
mo = greedy.findall(serve)
print(mo)

# Making Dot Match Newlines Too (with re.DOTALL)
prime = 'Serve the public trust.\nProtect the innocent.\nUpload the laws'
print(prime)

dotStar = re.compile(r'.*')
mo = dotStar.search(prime)
print(mo.group())

dotStar = re.compile(r'.*', re.DOTALL)
mo = dotStar.search(prime)
print(mo.group())

# re.IGNORECASE
vowelRegex = re.compile(r'[aeiou]')
mo = vowelRegex.search('Al, why does your programming book talk about RoboCop so much?')
print(mo.group())

mo = vowelRegex.findall('Al, why does your programming book talk about RoboCop so much?')
print(mo)

vowelRegex = re.compile(r'[aeiou]', re.I)
mo = vowelRegex.findall('Al, why does your programming book talk about RoboCop so much?')
print(mo)




