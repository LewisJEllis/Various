# Anything that seems like it could be reused in more than one problem goes here.

# Sieve of Eratosthenes, finds all primes less than n
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

def is_prime(n):
    if n < 2:
        return False
    return all([n % i != 0 for i in range(2,int(n**0.5+1))])

def is_prime_sieve(lim):
    # returns a function which can check primality of anything up to lim

    pl = sieve(int(lim**0.5)+1)
    pls = set(pl)

    def is_prime(n):
        if n in pls:
            return True

        stop = int(n**0.5)+1
        for p in pl:
            if n % p == 0:
                return False
            if p > stop:
                return True
        return True

    return is_prime

fl = [1,1,2,3,5]

# Returns the first n Fibonacci numbers
def fibs(n):
    while n > len(fl):
        fl.append(fl[-1] + fl[-2])
    return fl[:n]

def fib(n):
    while n > len(fl):
        fl.append(fl[-1] + fl[-2])
    return fl[n-1]

# '123' -> ['123','231', '312']
def rotations(s):
    for i in range(len(s)):
        yield s
        s = s[1:]+s[0]
