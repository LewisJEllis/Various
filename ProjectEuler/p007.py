"""
Project Euler #7
Lewis J Ellis

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?
"""

"""
Before writing this, I considered a sieve which could be faster, but would require an upper bound estimation function for the nth prime
Not knowing one off hand, I decided to just implement this fairly straightforward method.

After some further research, there are two possible improvements for time complexity:
1. Using nlogn + nloglogn as an upperbound approximation, and a sieve
2. Use a dictionary and some craftiness
But both of these have a significantly higher space-complexity than my solution
Additionally, I don't think the time complexity improvement is significant for n = 10001
So I'm just going to leave it be, since there's a reasonable tradeoff going on - and a sieve will probably be appropriate in a later problem anyway
Of course, this /could/ be done in nearly constant space, but the time complexity would be absurd.
"""

primes = [2,3,5,7,11,13,17,19,23,29] # start with at least [2,3], I only went to 29 so sprimes could be [2,3,5]
sprimes = [2,3,5] # primes up to the square root of n

n = primes[-1]
while len(primes) < 10001:
  n += 2
  if n ** 0.5 > sprimes[-1]:
    sprimes.append(primes[len(sprimes)])
  if all([n % p != 0 for p in sprimes]):
    primes.append(n)

print primes[-1]