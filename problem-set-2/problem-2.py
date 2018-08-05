# Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.
# In this problem, we will not be dealing with a minimum monthly payment rate.
# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal
# The monthly payment must be a multiple of $10 and is the same for all months.
# Notice that it is possible for the balance to become negative using this payment scheme, which is okay.

balance = 3329
annualInterestRate = 0.2

# Paste your code into this box

def calculateFinalBalance(originalBalance, payment):
  '''
  originalBalance: positive number, original balance
  payment: positive number, monthly payment, must be a multiple of 10

  returns: final balance after a year
  '''
  balance = originalBalance
  for month in range(0, 12):
    balance = (balance - payment) * (annualInterestRate / 12 + 1)
  return balance

def findPayment(balance, payment):
  '''
  balance: positive number
  payment: positive number, monthly payment, must be a multiple of 10
  '''
  finalBalance = calculateFinalBalance(balance, payment)
  if finalBalance > 0:
    return findPayment(balance, payment + 10)
  else:
    print('Lowest Payment:', payment)

findPayment(balance, 10)
