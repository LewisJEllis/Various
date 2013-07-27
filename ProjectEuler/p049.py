"""
Project Euler #49

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

# This could be done much more efficiently, but at the scale of 10^5 it doesn't matter at all
from helpers import isPrime

for i in range(1000,10000-6660):
    if isPrime(i):
        a = sorted(str(i))
        b = sorted(str(i + 3330))
        c = sorted(str(i + 6660))
        if a == b and a == c and isPrime(i+3330) and isPrime(i+6660):
            print i
            print i + 3330
            print i + 6660
