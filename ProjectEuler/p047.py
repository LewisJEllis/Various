from helpers import sieve

primes = sieve(10000)
lastn = 0
n = 644

while lastn < 4:
    n += 1
    if len([1 for i in primes if n % i == 0]) > 3:
        lastn += 1
    else:
        lastn = 0
print n-3