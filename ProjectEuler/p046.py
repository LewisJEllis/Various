def sieve(n):
  s = [False]*2 + [True]*(n-2)
  lim = len(s) ** 0.5
  for p,b in enumerate(s):
    if p > lim:
      break
    if not b:
      continue
    for i in range(2*p,len(s),p):
        s[i] = False
  return [i for (i, b) in enumerate(s) if b]

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