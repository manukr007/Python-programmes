# Guessing game
import random
guessesTaken = 0
print('Time to play a guessing game.')
print('Enter a number between 1 and 100:')
number = random.randint(1, 100)
while guessesTaken < 6:
    print('Take a guess.') 
    guess = input()
    guess = int(guess)
    guessesTaken = guessesTaken + 1
    if guess < number:
        print('Too low.')

    if guess > number:
        print('Too high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Congratulations! You got it in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)