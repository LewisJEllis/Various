from helpers import sieve

def rotations(s):
    for i in range(len(s)):
        yield s
        s = s[1:]+s[0]

primes = set(map(str, sieve(1000000)))
print len([p for p in primes if all([r in primes for r in rotations(p)])])