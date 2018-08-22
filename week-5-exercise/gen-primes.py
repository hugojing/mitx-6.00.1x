# Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...

def genPrimes():
  yield 2
  n = 3
  while True:
    isPrime = True
    for i in range(2, n):
      if n % i == 0:
        isPrime = False
        break
    if isPrime:
      yield n
    n += 1
