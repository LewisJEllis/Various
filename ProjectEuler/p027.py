from helpers import is_prime

def longest(a, b):
    n = 0
    while is_prime(n**2 + a*n + b):
        n += 1   
    return (n, a, b, a*b)

print reduce(max, [longest(a,b) for a in range(-1000,1001) for b in range(-1000,1001)])
