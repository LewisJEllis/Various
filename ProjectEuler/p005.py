"""
Project Euler #5
Lewis J Ellis

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
# Unique factorization and knowing how primes work make this simple:
# print 2520*11*13*2*17*19

"""
But that's no fun, so I came up with a factorization-based reduction alg; it's essentially a smart LCM finder.
It could be made nicer and generalized and refactored a bit, but speedwise it's fine.
Even doing each sequential number independently rather than on top of the previous ones,
It generates http://oeis.org/A003418 to 100 entries instantly, 500 in 1s, and 1000 in 3s.
Most of this time is spent in the sieve for repeatedly generating primes and iterating over the same things hundreds of times
So I think switching it around to not repeat itself could easily make it generate thousands of terms instantly.
For kicks: lcm(100000) took around 20 seconds and is 43452 digits long, and it holds that lcm(n) has ~ 0.434*n digits.
"""

from helpers import sieve
import math

def lcm(n):
  primes = sieve(n+1)
  l = range(1,n+1)
  r = 1
  for i in range(n):
    while r % l[i] != 0:
      for p in primes:
        if l[i] % p == 0:
          r *= p
    if r % l[i] == 0:
      continue
    j = 0
    while j < len(primes):
      p = primes[j]
      if l[i] % p == 0:
        l[i] /= p
        r *= p
      else:
        j += 1
  return r

print lcm(20)