# Can be smarter about this by thinking about factorization, but not by that much, and this runs instantly anyway
print len(set([a**b for a in range(2,101) for b in range(2,101)]))