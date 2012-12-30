"""
Project Euler #48
Lewis J Ellis

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

"""
Obviously there's some kind of neat way to do this with some number theory and modular arithmetic.
Someday I might revisit this and think about it more and do it that way.
But for now, python longs are good enough to brute through it instantly.
And this is a oneliner; even if it's not the best way to do it, it still looks kinda nice.
"""

print str(sum([i ** i for i in range(1, 1001)]))[-10:]