"""
Project Euler #10
Lewis J Ellis

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from helpers import sieve

print sum(sieve(2000000))