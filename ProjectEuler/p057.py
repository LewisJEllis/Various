c, ln, n, ld, d = 0, 1, 1, 0, 1
for i in range(1000):
    ln, n, ld, d = n, n*2 + ln, d, d*2 + ld
    c += int(len(str(n)) > len(str(d)))
print c