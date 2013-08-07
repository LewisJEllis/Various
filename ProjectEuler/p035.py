from helpers import sieve, rotations
primes = set(map(str, sieve(1000000)))
print len([p for p in primes if all([r in primes for r in rotations(p)])])