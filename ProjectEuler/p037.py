# This is really dumb and takes forever to run, I know
from helpers import sieve, isPrime
print sum([int(p) for p in map(str,sieve(1000000)[4:]) if all([isPrime(int(p[i:])) and isPrime(int(p[:i+1])) for i in range(len(p))])])