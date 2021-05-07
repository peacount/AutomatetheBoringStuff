# Raising your own exceptions
"""
****************************
*                          *
*                          *
*                          *
****************************

"""
def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception ('"symbol" needs to be a string of length 1')
    if (width < 2) or (height < 2):
        raise Exception ('"width" and "height" need to be greater or equal to 2')
    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width -2) + symbol))
    
    print(symbol * width)

boxPrint ('*', 15, 5)
boxPrint ('O', 5, 20)
boxPrint ('**', 15, 5)
boxPrint ('*', 1, 1)

# The traceback.format_exc() Function
import traceback 
try:
    raise Exception ('this is the error message.')
except: 
    errorFile = open('error_log.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written in the error_log.txt')

import os
print(os.getcwd())
