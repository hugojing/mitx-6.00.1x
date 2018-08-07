# For each of the following questions (which you may assume is evaluated independently of the previous questions, so that testList has the value indicated above), provide an expression using applyToEach, so that after evaluation testList has the indicated value.
# You may need to write a simple procedure in each question to help with this process.

def applyToEach(L, f):
  for i in range(len(L)):
    L[i] = f(L[i])

testList = [1, -4, 8, -9]

# [1, 4, 8, 9]
# Your Code Here
applyToEach(testList, abs)


# [2, -3, 9, -8]
# Your Code Here
def addOne(e):
  return e + 1

applyToEach(testList, addOne)


# [1, 16, 64, 81]
# Your Code Here
def square(e):
  return e ** 2

applyToEach(testList, square)
