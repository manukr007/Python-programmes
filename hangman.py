#Hangman

import random
print ('Welcome to hangman. You get seven chances to guess the mystery word.')
word = 'bat','cat','rat'
secret = random.choice(word)
guesses = ''
turns = 5

while turns > 0:
  missed = 0
  for letter in secret:
    if letter in guesses:
      print (letter,)
    else:
      print ('_',)
      missed += 1

  if missed == 0:
    print ('You win!')
    break

  guess = input('guess a letter: ')
  guesses += guess

  if guess not in secret:
    turns -= 1
    print ('Nope.')
    print (turns, 'more turns')
    if turns < 5: print ('   O   ')
    if turns < 4: print (' \_|_/ ')
    if turns < 3: print ('   |   ')
    if turns < 2: print ('  / \  ')
    if turns < 1: print (' d   b ')
    if turns == 0:
      print ('The answer is', secret)