# we can use the idea of bisection search to determine if a character is in a string, so long as the string is sorted in alphabetical order.
# Implement the function isIn(char, aStr) which implements the above idea recursively to test if char is in aStr.
# char will be a single character and aStr will be a string that is in alphabetical order.
# The function should return a boolean value.

def isIn(char, aStr):
  '''
  char: a single character
  aStr: an alphabetized string
  
  returns: True if char is in aStr; False otherwise
  '''
  # Your code here
  char = char.lower()
  aStr = aStr.lower()
  index = int(len(aStr) / 2)
  if aStr == '':
    return False
  elif index == 0:
    return char == aStr[0]
  elif char < aStr[index]:
    aStr = aStr[0:index]
    return isIn(char, aStr)
  else:
    aStr = aStr[index:]
    return isIn(char, aStr)
