import re

# The sub() Method
namesRegex = re.compile(r'Agent \w+')
mo = namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.')
print(mo)

mo = namesRegex.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob.')
print(mo)

# Using\1, \2, etc in sub()
namesRegex = re.compile(r'Agent (\w)\w*')
mo = namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.')
print(mo)

mo = namesRegex.sub(r'Agent \1****','Agent Alice gave the secret documents to Agent Bob.')
print(mo)

# Verbose Mode with re.VERBOSE
re.compile(r'''
(\d\d\d)|     # area code (without parens)
(\(\d\d\d\) ) # -or- area code with parens and no dash 
-             # second dash
\d\d\d\d      # last 4 digits
\sx\d{2,4}    # extension, like x1234''', re.VERBOSE)

# Using Multiple Options (re.I, re.DOTALL, re.VERBOSE)
re.compile(r'''
(\d\d\d)|     # area code (without parens)
(\(\d\d\d\) ) # -or- area code with parens and no dash 
-             # second dash
\d\d\d\d      # last 4 digits
\sx\d{2,4}    # extension, like x1234''', re.I | re.DOTALL | re.VERBOSE) # | bitwise operator


