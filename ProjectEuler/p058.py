from helpers import is_prime_sieve

def term(m,n):
    #mth term along nth diagonal
    return 1 + (2*n)*m + 4*(m-1)*m

is_prime = is_prime_sieve(term(13121,4))

m = 0
termcount = 0
while True:
    m += 1
    termcount += len([1 for n in range(1,5) if is_prime(term(m,n))])
    ratio = termcount/(m*4.0+1)
    if ratio < 0.10:
        print m*2+1, ratio
        break
