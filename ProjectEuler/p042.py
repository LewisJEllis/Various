words = eval('[' + open('p042words.txt', 'r').readlines()[0] + ']')
s = set([i*i for i in range(1,40)])
# Not sure which way I like better here
print sum(1 for w in words if 1+8*sum([ord(i)-64 for i in w]) in s)
print len(filter(lambda w: 1+8*sum([ord(i)-64 for i in w]) in s, words))