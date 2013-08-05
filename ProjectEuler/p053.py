import math

def nck(n,k):
    f = math.factorial
    return f(n)/f(k)/f(n-k)

print len([1 for n in range(23,101) for k in range(3,n-2) if nck(n,k) > 1000000])