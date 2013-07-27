from helpers import sieve

primes = sieve(10000)
doublesquares = [2*n**2 for n in range(100)]

for n in range(33, 10000, 2):
    works = False
    for p in primes:
        if (n - p) in doublesquares:
            works = True
            break
    if not works:
        print n, 'doesnt work'
        break