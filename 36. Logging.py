# logging.debug() -- the lowest level
import logging
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Logging to a Text File
logging.basicConfig(filename = 'myProgramLog.txt', format='%(asctime)s - %(levelname)s - %(message)s')

# logging.disable(loggig.CRITICAL)
# logging.disable(logging.CRITICAL)

# The logging debug function
logging.debug ('START OF Program')

# Buggy Facotrial Example
def factorial(n):
    logging.debug('start of factorial(%s)' % (n))
    total = 1
    for i in range(1, n+1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))

    logging.debug('return value is %s' % (total))
    return total
    
print(factorial(5))    

logging.debug ('End OF Program') 

# logging.info()
# logging.warning()
# logging.error()
# logging.critical()


