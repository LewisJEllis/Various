to1 = set([44, 32, 13, 10, 1])
to89 = set([85,89,145,42,20,4,16,37,58])
t = 0

for i in range(2, 10000000):
    while True:
        ni = sum([int(d)**2 for d in str(i)])
        if ni in to89:
            t += 1
            if i < 568:
                to89.add(i)
            break
        elif ni in to1:
            if i < 568:
                to1.add(i)
            break
        i = ni

print t