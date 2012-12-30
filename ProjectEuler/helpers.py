"""
Project Euler Helpers
Lewis J Ellis

Anything that seems like it could be reused in more than one problem goes here.
"""

"""
Sieve of Eratosthenes. Originally written for #10.
This can be made nicer, but this is what I came up with the first time through.
Using a list lets you get by with only O(1) operations; other structures can yield more elegant code, but will use slower operations
Particularly, this method does lots of enumerating and re-iterating which other datastructures can avoid
I think some craftiness combined with a list of ints instead of a list of bools can clean this up.
But this is easy to read and makes sense, so I'll leave it be until I need a bleeding edge sieve.
"""
def sieve(n):
  s = [False]*2 + [True]*(n-2)
  lim = len(s) ** 0.5 # I wonder if python's interpreter would make this only-compute-the-sqrt-once optimization on its own?
  # I also wonder, since the loop mainly just uses p, if it's faster to enumerate, or use i in xrange(n), and replace p = i, b = s[i]?
  for p,b in enumerate(s):
    if p > lim:
      break
    if not b:
      continue
    m = 2
    while m*p < len(s): # probably a way to do this with for .. range?
      s[m*p] = False
      m += 1
  return [i for (i, b) in enumerate(s) if b]

def isPrime(n):
  if n < 2:
    return False
  for i in range(2,int(n**0.5+1)):
    if n % i == 0:
      return False
  return True

def isPrimeSieve(n):
  s = sieve(int(n**0.5+1))
  for p in s:
    if n % p == 0:
      return False
  return True
