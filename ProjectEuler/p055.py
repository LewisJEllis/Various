def lychrel(n):
    n = str(n)
    for i in range(50):
        n = str(int(n) + int(n[::-1]))
        if n == n[::-1]:
            return False
    return True

print sum([1 for i in range(10000) if lychrel(i)])