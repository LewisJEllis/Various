# This is really dumb and takes forever to run, I know
# A smarter way would just check random combos matching ([3,7,9][1,3,7,9]*[3,7,9]) until you find 11
from helpers import sieve, isPrime
print sum([int(p) for p in map(str,sieve(1000000)[4:]) if all([isPrime(int(p[i:])) and isPrime(int(p[:i+1])) for i in range(len(p))])])