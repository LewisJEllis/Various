"""
Project Euler #30
Lewis J Ellis

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

# We get an upper bound by observing 6*9^5 = 354294
# There can't be anything bigger because 7*9^5 < the smallest 7 digit number
# From there I just brutishly onelinered it. Runs in a second or two.

print sum([i for i in xrange(10,354294) if i == sum([int(c)**5 for c in str(i)])])
