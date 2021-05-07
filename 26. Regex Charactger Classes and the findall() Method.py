import re
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# The findall() Method
resume = """ JANE SOMEBODY
123 Anywhere Street, City, State
555-000-0000, 123-456-2098
janesomebody@emailprovider.com

PROFILE

State the type of job you are seeking and highlight several of your most important, impressive and marketable skills.

SUMMARY OF SKILLS

- Include your most marketable skills and accomplishments here.
- Ensure the skills you list are relevant to the type of job you are seeking.
- Be as specific as possible. """

print(phoneRegex.findall(resume))

phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
print(phoneRegex.findall(resume))

phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
print(phoneRegex.findall(resume))

# Character Classes (Table 7-1)
lyrics = '12 drummers drumming, 11 pipers piping, 10 lords a-leaping, 9 ladies dancing, 8 maids a-milking, 7 swans a-swimming, 6 geese a-laying, 5 golden rings, 4 calling birds, 3 french hens, 2 turtle doves, and 1 partridge in a pear tree'

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(lyrics))

# Making your own character classes
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('Robocop eats baby food.'))

doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')
print(doubleVowelRegex.findall('Robocop eats baby food.'))

# Negative Character Classes
consonantsRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantsRegex.findall('Robocop eats baby food.'))
