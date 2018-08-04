# A regular polygon has n number of sides. Each side has length s.
# Write a function called polysum that takes 2 arguments, n and s.
# This function should sum the area and square of the perimeter of the regular polygon.
# The function returns the sum, rounded to 4 decimal places.

import math

def polysum(n, s):
  '''
  n, s: positive numbers

  returns: number, the sum the area and square of the perimeter.
  '''
  area = 0.25 * n * s ** 2 / math.tan(math.pi / n)
  square = (n * s) ** 2
  return round(area + square, 4)
