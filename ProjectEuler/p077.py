# I could probably improve this to not recalculate n(v) over and over but instead build it all at once
# But I had basically already written n(v) for solving the earlier coin problem, and it was easy to reuse

from helpers import sieve
primes = sieve(100)

def n(v):
    ways = [1]+[0]*v
    for prime in primes:
        for i in range(prime, v+1):
            ways[i] += ways[i-prime]
    return ways[v]

v = 2
while n(v) < 5000:
    v += 1
print v, n(v)