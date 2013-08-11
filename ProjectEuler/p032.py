import itertools

# Alternate: iterate over the 9p4 possible products
# Then iterate over the 5! orders of the remaining 5 and see if any make the product
# That would definitely be faster, but this is easier to code and still fast enough

s, found = 0, set()

for p in itertools.permutations('123456789'):
    for i in range(1,3):
        p1 = int(''.join(p[0:i]))
        p2 = int(''.join(p[i:5]))
        p3 = int(''.join(p[5:]))
        if p3 not in found and p1*p2 == p3:
            print '%s * %s = %s' % (p1,p2,p3)
            s += p3
            found.add(p3)
print s