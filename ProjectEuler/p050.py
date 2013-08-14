from helpers import sieve, isPrime

p = sieve(10000)

total = 0
start = 0
length = 0
maxlen = 0
while True:
    if total + p[start+length] < 1000000:
        total += p[start+length]
        length += 1
        if length > maxlen and isPrime(total):
            if 1000000 - total < p[start+length]:
                print total
                break
            maxlen = length
    else:
        total -= (p[start] + p[start+length-1])
        length -= 2
        start += 1