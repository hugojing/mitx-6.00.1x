# We want to write some simple procedures that work on dictionaries to return information.
# This time, write a procedure, called biggest, which returns the key corresponding to the entry with the largest number of values associated with it.
# If there is more than one such entry, return any one of the matching keys.
# >>> biggest(animals)
# 'd'

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
  '''
  aDict: A dictionary, where all the values are lists.

  returns: The key with the largest number of values associated with it
  '''
  # Your Code Here
  for key in aDict:
    aDict[key] = len(aDict[key])
  
  target = max(aDict.values())
  if target == 0:
    return 'None'
    
  for key in aDict:
    if aDict[key] == target:
      return key

print(biggest(animals))
