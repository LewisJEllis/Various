def n(p):
    coins = [1,2,5,10,20,50,100,200]
    ways = [1]+[0]*p 
    for coin in coins:
        for i in range(coin, p+1):
            ways[i] += ways[i-coin]
    return ways[p]

for i in [1,2,83,159,146,200]:
    print n(i)