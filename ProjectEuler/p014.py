# Could do this more efficiently with a tree structure.
def chain_length(n):
    steps = 0
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = n*3+1
        steps += 1
    return steps

print max([(chain_length(i),i) for i in range(1000000)])