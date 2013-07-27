# Anything that seems like it could be reused in more than one problem goes here.

# Sieve of Eratosthenes
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

def isPrime(n):
    return all([n > 1] + [n % i != 0 for i in range(2,int(n**0.5+1))])

def isPrimeSieve(n):
    return all([n % p != 0 for p in sieve(int(n**0.5+1))])

fl = [1,1,2,3,5]

def fibs(n):
    while n > len(fl):
        fl.append(fl[-1] + fl[-2])
    return fl[:n]

def fib(n):
    while n > len(fl):
        fl.append(fl[-1] + fl[-2])
    return fl[n-1]
