#Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

from helpers import sieve

p = sieve(1000)[3:]

def cyclelen(n):
    k = 1
    while True:
        if 10**k % n == 1:
            return (k, n)
        k += 1

print max(map(cyclelen, p))
