from helpers import isPrime

for i in range(1000,10000-6660):
    if isPrime(i):
        a = sorted(str(i))
        b = sorted(str(i + 3330))
        c = sorted(str(i + 6660))
        if a == b == c and isPrime(i+3330) and isPrime(i+6660):
            print i, i + 3330, i + 6660
