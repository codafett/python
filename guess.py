import random

while True:
  target = random.randint(1, 10)
  guess = 0
  while guess != target:
    guess = int(input('Guess a number between 1 and 10: '))
    if guess < target:
      print('Too low, try again!')
    elif guess > target:
      print('Too high, try again!')
    else:
      print('You guessed it! ?You won!')
  play = input('Play again (y/n)? ')
  if play == 'n':
    print('*** GAME OVER ***')
    break