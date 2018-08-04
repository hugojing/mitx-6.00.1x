# Write an iterative function, gcdIter(a, b), that implements this idea.
# One easy way to do this is to begin with a test value equal to the smaller of the two input arguments, and iteratively reduce this test value by 1 until you either reach a case where the test divides both a and b without remainder, or you reach 1.

def gcdIter(a, b):
  '''
  a, b: positive integers
  
  returns: a positive integer, the greatest common divisor of a & b.
  '''
  # Your code here
  while b != 0:
    result = b
    b = a % b
    a = result
  return a
