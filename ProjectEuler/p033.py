result = 1
for i in range(10,100):
    for j in range(i,100):
        if i != j:
            for (a,b) in [(1,0),(0,1),(1,1)]:
                si, sj = str(i), str(j)
                # if we can cancel two things nontrivially
                if si[a] == sj[b] and si[a] != '0':
                    # and that ends up being equal
                    if sj[1-b] != '0' and float(si[1-a])/int(sj[1-b]) == 1.0*i/j:
                        result *= 1.0*i/j
print 1/result