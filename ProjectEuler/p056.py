print reduce(max, (sum(map(int,str(a**b))) for a in range(2,100) for b in range(2,100)))
