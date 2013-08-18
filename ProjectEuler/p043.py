import itertools

total = 0
for p in itertools.permutations('0123456789'):
    n = ''.join(p)
    if all([int(n[i:i+3]) % [2,3,5,7,11,13,17][i-1] == 0 for i in range(1, 8)]):
        total += int(n)
        print n
print total
