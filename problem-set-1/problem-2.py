# Assume s is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' occurs in s.
# For example, if s = 'azcbobobegghakl', then your program should print
# Number of times bob occurs is: 2

s = 'azcbobobegghakl'

# Paste your code into this box

count = 0
index = 0

for letter in s:
  if letter == 'b':
    if index <= len(s) - 3:
      if s[index + 1] == 'o' and s[index + 2] == 'b':
        count += 1
  index += 1

print('Number of times bob occurs is:', count)
