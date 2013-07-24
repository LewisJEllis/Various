def factorize(n):
  if n == 1: return [1]
  divs = [2] + range(3,n+1,2)
  i, factors = 0, []
  while divs[i] <= (n/2):
    while (n % divs[i]) == 0:
      n //= divs[i]
      factors.append(divs[i])
    i += 1
  if n != 1: factors.append(n)
  return factors

def factorize_distinct(n):
  if n == 1: return [1]
  divs = [2] + range(3,n+1,2) #2,3,5,7...
  i, factors = 0, []
  while divs[i] <= (n/2):
    power = 0
    while (n % divs[i]) == 0:
      n //= divs[i]
      power += 1
    if power > 0:
      factors.append(divs[i])
    i += 1
  if n != 1: factors.append(n)
  return factors

r = [len(factorize(n)) for n in range(1,1001)]
print([r.count(n) for n in range(1,10)])
r = [len(factorize_distinct(n)) for n in range(1,1001)]
print([r.count(n) for n in range(1,5)])
