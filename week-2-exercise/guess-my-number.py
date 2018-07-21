# Exercise: guess my number
# The program works as follows:
# you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive).
# The computer makes guesses, and you give it input - is its guess too high or too low?
# Using bisection search, the computer will guess the user's secret number!

# Paste your code into this box

print('Please think of a number between 0 and 100!')

x = 0
y = 100

while True:
  guess = int((x + y) / 2)
  print('Is your secret number ', end = '')
  print(guess, end = '')
  print('?')
  answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
  if (answer == 'h'):
    y = guess
  elif (answer == 'l'):
    x = guess
  elif (answer == 'c'):
    print('Game over. Your secret number was: ', end = '')
    print(guess)
    break
  else:
    print('Sorry, I did not understand your input.')
