# Write a function gcdRecur(a, b) that implements this idea recursively.
# This function takes in two positive integers and returns one integer.

def gcdRecur(a, b):
  '''
  a, b: positive integers
  
  returns: a positive integer, the greatest common divisor of a & b.
  '''
  # Your code here
  if b == 0:
    return a
  else:
    return gcdRecur(b, a % b)
