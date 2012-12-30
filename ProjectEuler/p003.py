"""
Project Euler #3
Lewis J Ellis

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

n = 600851475143
i = 3
# I'm ignoring evens since our input is odd. If it were even, we could reduce it to an odd input before this loop.
# Basically, iterate over odds, divide n by every odd that goes into it until n = 1
# When that happens, you just divided by the biggest prime factor, so stop and print it.
while n > 1:
  if n % i == 0:
    n /= i
  else:
    i += 2
print i