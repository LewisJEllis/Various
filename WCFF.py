"""
Will Code For Food challenge done at Penn
5 problems given, increasingly desirable food rewards for solving each.
It was a fun event. This is what I wrote to win my food.

"""

def fibsum(max):
  s = 1
  p1 = 0
  p2 = 1
  n = p1 + p2
  while n <= max:
    s += n
    p1 = p2
    p2 = n
    n = p1 + p2
  return s

print fibsum(1)
print fibsum(2)
print fibsum(100)
print fibsum(200)
print fibsum(15000) 


primes = [2,3,5,7,11,13,17,19,23,29] # start with at least [2,3], I only went to 29 so sprimes could be [2,3,5]
sprimes = [2,3,5] # primes up to the square root of n

n = primes[-1]
while len(primes) < 4554:
  n += 2
  if n ** 0.5 > sprimes[-1]:
    sprimes.append(primes[len(sprimes)])
  if all([n % p != 0 for p in sprimes]):
    primes.append(n)

print primes[0]
print primes[1]
print primes[98]
print primes[830]
print primes[4551]
#2,3,541,6379,43711

def n(p):
  coins = [1,2,5,10,20,50,100,200]
  ways = [1]+[0]*p 
  for coin in coins:
    for i in range(coin, p+1):
      ways[i] += ways[i-coin]
  return ways[p]

for i in [1,2,83,159,146]:
  print n(i)

"""
1,2,2326,27680,19575
"""

def spell(n):
  tens = [None, None, "twenty", "thirty", "forty",
          "fifty", "sixty", "seventy", "eighty", "ninety"]
  small = ["zero", "one", "two", "three", "four", "five",
           "six", "seven", "eight", "nine", "ten", "eleven",
           "twelve", "thirteen", "fourteen", "fifteen",
           "sixteen", "seventeen", "eighteen", "nineteen"]

  if n == 1000:
    return "one thousand"

  def rest(c, n):
    return "" if n == 0 else c + spell(n)
  if n < 20:
    return small[n]
  elif n < 100:
    a, b = divmod(n, 10)
    return tens[a] + rest(" ", b)
  elif n < 1000:
    a, b = divmod(n, 100)
    return small[a] + " hundred and" + rest(" ", b)

def nsl(s):
  return len("".join(s.split()))

for i in [1,5,83,121,568,957,1000]:
  print spell(i), nsl(spell(i))

#3,4,11,22,24,24,11

from sys import maxint

def minchanges(max, dna):
  nucs = "ACGT"
  r = maxint
  for period in xrange(1, max+1):
    t = 0
    for i in xrange(0, period):
      nucCounts = [0,0,0,0]
      total = 0
      for j in xrange(i, len(dna), period):
        nucCounts[nucs.index(dna[j])] += 1
        total += 1
      cur = maxint
      for (j, count) in enumerate(nucCounts):
        cur = min(cur, total - count)
      t += cur
    r = min(r, t)
  return r
print minchanges(3, "ATAGATA")
print minchanges(12, "ACGTATAGCATGACAACAGATATTATGACAGATGTAGCAGTAACCAGAC")
print minchanges(8, "ACTGACTGACTGGACTACC")
print minchanges(5, "ACTGGAGAGATCATCATATA")


import math

def minlength(x,y):
  if math.e ** (x/math.e) < y:
    return -1
  n = 2
  while (float(x)/n)**n < y:
    n += 1
  return n

for (x,y) in [(5,6),(5,100),(100,10000),(50,40000000)]:
  print minlength(x,y)




