# Anything outside 9234-9487 either is smaller than 918273645 or has 2 1's or has 2 9's
print max([100002*i for i in range(9234,9388) if set(list(str(100002*i))) == set(list('123456789'))])
