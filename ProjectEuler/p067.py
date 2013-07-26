t = [map(int, line.split()) for line in open('p067triangle.txt', 'r').readlines()]

while len(t) > 1:
    for i in range(len(t[-2])):
        t[-2][i] += max(t[-1][i], t[-1][i+1])
    t.pop()
print t[0][0]