import math

f1, f2, n = 1, 1, 2
while math.log10(f2)+1 < 1000:
    f1, f2, n = f2, f1 + f2, n + 1
print n
