# Assume s is a string of lower case characters.
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
# For example, if s = 'azcbobobegghakl', then your program should print
# Longest substring in alphabetical order is: beggh

# In the case of ties, print the first substring.
# For example, if s = 'abcbcd', then your program should print
# Longest substring in alphabetical order is: abc

s = 'azcbobobegghakl'

# Paste your code into this box
from functools import reduce

# give weight by alphabetical order for every letter of s
l = list(set(s))
l.sort()
arr = []

for letter in s:
  arr.append([{
    'value': letter,
    'weight': l.index(letter)
  }])

# split s to substrings by weight
substrings = []

def splitSubstring(x, y):
  if len(x) == 0 or x[-1]['weight'] <= y[0]['weight']:
    x.append(y[0])
    return x
  else:
    substrings.append(x)
    return y
  
last = reduce(splitSubstring, arr)
substrings.append(last)

# find the first longest substring
indexs = []

for ele in substrings:
  indexs.append(len(ele))

index = indexs.index(max(indexs))

answer = ''

for ele in substrings[index]:
  answer += ele['value']

print('Longest substring in alphabetical order is:', answer)
