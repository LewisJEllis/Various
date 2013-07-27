# This kind of follows how I thought the solution out
def printSum(n):
    s = 2*n-1
    m = (n-1)/2
    print "sum of diagonals of %sx%s snake grid:" % (n,n)
    for i in range(2,(n-1)*4-5,8):
        print "  (%s+%s+%s+%s)*%s +" % (i, i+2, i+4, i+6, m)
        s += (4*i+12)*m
        m -= 1
    print "  %s = %s" % (2*n-1, s)
printSum(5)

# And here's the dense one-liner version, for kicks:
n = 1001
print 2*n-1 + sum([(4*v+12)*((n-1)/2-i) for i,v in enumerate(xrange(2,n*4-9,8))])
