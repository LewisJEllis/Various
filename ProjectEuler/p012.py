def d(n):
    return len([i for i in range(1,int(n**0.5)+1) if n % i == 0])*2

tn = 1
n = 1
while d(tn) < 500:
    n += 1
    tn += n
print tn
