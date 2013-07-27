"""
Project Euler #28
Lewis J Ellis

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
43              49
  21 22 23 24 25
  20  7  8  9 10
  19  6  1  2 11
  18  5  4  3 12
  17 16 15 14 13
37              31
It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

"""
Looking at the differences along the diagonals reveals a fairly simple set of sequences.
Now we just take the sum of those sequences to 500 terms each.
Here's the verbose method which represents the thoughts in coming to the solution
"""

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
