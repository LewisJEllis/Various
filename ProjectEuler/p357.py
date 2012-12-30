"""
Project Euler #357
Lewis J Ellis

Consider the divisors of 30: 1,2,3,5,6,10,15,30.
It can be seen that for every divisor d of 30, d+30/d is prime.

Find the sum of all positive integers n not exceeding 100 000 000
such that for every divisor d of n, d+n/d is prime.
"""

"""
The case d = n, which requires n + n/n be prime, tells us every n is one less than a prime
So our candidate set is reduced to primes below 100,000,000, of which there are 5,761,455
"""