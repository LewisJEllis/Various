s = [n**2 for n in range(1002)]

def count(p):
    return sum([1 for l1 in range(p/2) for l2 in range(l1,p/2) if s[l1]+s[l2] == s[p-l1-l2]])

print max((count(p),p) for p in range(120,1001))
