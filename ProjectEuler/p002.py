from helpers import fibs

print sum([f for f in fibs(50) if f % 2 == 0 and f < 4000001])
