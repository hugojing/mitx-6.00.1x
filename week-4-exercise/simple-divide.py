# Your task is to change the definition of simple_divide so that the call does not raise an exception.
# When dividing by 0, should return a 0 element.
# Any other error cases should still raise exceptions.
# You should only handle the ZeroDivisionError.

#define the simple_divide function here

def simple_divide(item, denom):
  try:
    return item / denom
  except ZeroDivisionError:
    return 0
