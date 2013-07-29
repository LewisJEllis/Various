import math
# 9!*7 is an easy upper bound, so let's just use that
print sum([i for i in range(10,2540161) if i == sum([math.factorial(d) for d in map(int,str(i))])])