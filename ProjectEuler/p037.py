# This is really dumb and takes forever to run, I know
# A smarter way would just check random combos matching ([3,7,9][1,3,7,9]*[3,7,9]) until you find 11
from helpers import sieve, is_prime
print sum([int(p) for p in map(str,sieve(1000000)[4:]) if all([is_prime(int(p[i:])) and is_prime(int(p[:i+1])) for i in range(len(p))])])