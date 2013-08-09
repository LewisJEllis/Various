n = 7830457
v = 1
while n > 0:
    i = max(n, 50)
    n -= i
    v = (v * 2**i) % (10**10)

print 28433*v+1