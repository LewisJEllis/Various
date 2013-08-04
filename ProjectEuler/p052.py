# I didn't actually think about this much before coding it
# But looking back, the answer seems rather obvious.
import math
n = 1000
while True:
    s = set(list(str(n)))
    if set(list(str(n*2))) == s:
        if s == set(list(str(n*3))) == set(list(str(n*4))) == set(list(str(n*5))) == set(list(str(n*6))):
            print n
            break
    if n/(10**math.floor(math.log10(n))) > (float(5)/3):
        n = int(10**math.ceil(math.log10(n)))
    else:
        n += 1