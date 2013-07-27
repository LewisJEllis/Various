# Knowing how unique factorization and primes work makes this simple:
# print 2520*11*13*2*17*19
# But that's no fun, so I here's a factorization-based reduction alg; it's essentially an LCM finder.
# It's not the smartest method, but it generates http://oeis.org/A003418 to 100 entries instantly, 500 in 1s, and 1000 in 3s.
# For kicks: lcm(100000) is 43452 digits long, and it holds that lcm(n) has ~ 0.434*n digits.

from helpers import sieve

def lcm(n):
    primes = sieve(n+1)
    l = range(1,n+1)
    r = 1
    for i in range(n):
        while r % l[i] != 0:
            for p in primes:
                if l[i] % p == 0:
                    r *= p
        if r % l[i] == 0:
            continue
        j = 0
        while j < len(primes):
            p = primes[j]
            if l[i] % p == 0:
                l[i] /= p
                r *= p
            else:
                j += 1
    return r

print lcm(20)
print lcm(100)
print lcm(1000)