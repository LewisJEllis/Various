from operator import mul
print(reduce(mul, [int(''.join([str(i) for i in range(200000)])[10**n]) for n in range(7)]))
