# Write a Python function, fourthPower, that takes in one number and returns that value raised to the fourth power.
# You should use the square procedure that you defined in an earlier exercise.

# Your code here

from square import square

def fourthPower(x):
  '''
  x: int or float.
  '''
  return square(square(x))
