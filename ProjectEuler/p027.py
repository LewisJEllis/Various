from helpers import isPrime

def longest(a, b):
    n = 0
    while isPrime(n**2 + a*n + b):
        n += 1   
    return (n, a, b, a*b)

print reduce(max, [longest(a,b) for a in range(-1000,1001) for b in range(-1000,1001)])
