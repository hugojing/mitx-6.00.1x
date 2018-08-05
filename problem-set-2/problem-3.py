# Write a program that uses these bounds and bisection search to find the smallest monthly payment to the cent (no more multiples of $10) such that we can pay off the debt within a year.
# Try it out with large inputs, and notice how fast it is (try the same large inputs in your solution to Problem 2 to compare!).
# Produce the same return value as you did in Problem 2.

balance = 40937
annualInterestRate = 0.21
# expected 3746.24 +/- 0.2

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

def findPayment(balance, paymentRange, isBisection = False, payment = 0):
  '''
  balance: positive number
  paymentRange: a range of monthly payment
  isBisection: boolean value, default is false
  payment: positive number,  monthly payment
  '''
  if isBisection:
    payment = payment
  else:
    payment = int((paymentRange[0] + paymentRange[-1]) / 2)

  finalBalance = calculateFinalBalance(balance, payment)

  if abs(int(finalBalance)) <= 1:
    print('Lowest Payment:', round(payment, 2))
  elif abs(finalBalance) <= 5 and finalBalance <= 0:
    return findPayment(balance, [], True, payment - 0.01)
  elif abs(finalBalance) <= 100 and finalBalance <= 0:
    return findPayment(balance, [], True, payment - 0.1) 
  elif finalBalance > 0:
    return findPayment(balance, range(payment, paymentRange[-1]))
  elif finalBalance < 0:
    return findPayment(balance, range(paymentRange[0], payment))

paymentRange = range(int(balance / 12), int(balance * (1 + annualInterestRate / 12) ** 12 / 12))
findPayment(balance, paymentRange)
