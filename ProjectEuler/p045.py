def t(n):
    return n*(n+1)/2

def p(n):
    return n*(3*n-1)/2

def h(n):
    return n*(2*n-1)


lim = 100000
ts = set([t(n) for n in range(286,lim)])
ps = set([p(n) for n in range(286,lim)])
hs = set([h(n) for n in range(286,lim)])

print ts & ps & hs