from helpers import is_prime_sieve
is_prime = is_prime_sieve(10000)

for i in range(1000,10000-6660):
    if is_prime(i):
        a = sorted(str(i))
        b = sorted(str(i + 3330))
        c = sorted(str(i + 6660))
        if a == b == c and is_prime(i+3330) and is_prime(i+6660):
            print i, i + 3330, i + 6660
