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

assert False, 'This is the error message.'

# Assertions and the assert statement
market_2nd = {'ns': 'green', 'ew': 'red'}

def switchLights(intersection): 
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] == 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] == 'red'
        elif intersection[key] == 'red':
            intersection[key] == 'green'
    assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)

print(switchLights(market_2nd))





