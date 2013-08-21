import itertools
from helpers import is_prime_sieve

is_prime = is_prime_sieve(7654321)

print reduce(max, filter(is_prime, map(lambda x: int(''.join(x)), itertools.permutations('1234567'))))
