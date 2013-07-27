"""
Project Euler #48
Lewis J Ellis

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

# There's probably a nicer way to do this with a little number theory and modular arithmetic
# But this is a oneliner and I like oneliners.

print str(sum([i ** i for i in range(1, 1001)]))[-10:]