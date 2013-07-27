# We get an upper bound by observing 6*9^5 = 354294
# There can't be anything bigger because 7*9^5 < the smallest 7 digit number
# Then I just used that upper bound to try everything.
print sum([i for i in xrange(10,354294) if i == sum([int(c)**5 for c in str(i)])])
