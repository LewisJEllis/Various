n = eval('[' + open('p022names.txt', 'r').readlines()[0] + ']')
n.sort()
print sum([sum([(j+1)*(ord(i)-64) for i in n[j]]) for j in range(len(n))])
