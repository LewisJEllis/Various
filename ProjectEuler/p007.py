# A sieve could be better at this, but requires a good estimate on the upper bound of the nth prime which I didn't know off hand
primes = [2,3,5,7,11,13,17,19,23,29]
sprimes = [2,3,5] # primes up to the square root of the biggest prime in primes

n = primes[-1]
while len(primes) < 10001:
    n += 2
        if n ** 0.5 > sprimes[-1]:
            sprimes.append(primes[len(sprimes)])
    if all([n % p != 0 for p in sprimes]):
        primes.append(n)

print primes[-1]

# I later found that nlogn + nloglogn is a good upperbound approximation:
from math import log
from helpers import sieve
n = 10001
print sieve(int(n*log(n) + n*log(log(n))))[10000]