def d(n):
    return sum([i for i in range(1,n/2+1) if n % i == 0])

print sum([n for n in range(10000) if n != d(n) and n == d(d(n))])