import itertools
from helpers import sieve
# rewrite isprimesieve to take a max
# write a better sieve?
pl = sieve(33334)
def prime(n):
    return all(n%p != 0 for p in pl)
l = filter(prime, map(lambda x: int(''.join(x)), itertools.permutations('1234567')))
print reduce(max,l)
