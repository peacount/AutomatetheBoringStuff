import random
print('Hello. What is your name?')
name=input()
secretNumber = random.randint(1,20)
print('Well, ' + name + ' , I am thinking of a number between 1 and 20')

print ('DEBUG: Secredit number is', secretNumber)

for guessesTaken in range (1,7):
    print('Take a guess.')
    guess = int(input())
    if guess < secretNumber:
        print ('Your guess is too low')
    elif guess > secretNumber:
        print ('Your guess is too high')
    else:
        break

if guess == secretNumber:
    print ('Good job, ' +  name + '! you guessed my number in', guessesTaken)
else:
    print ('Nope.  The number I was thinking of was ', secretNumber)