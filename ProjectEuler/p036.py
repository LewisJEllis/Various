print sum([n for n in range(1000000) if n == int(str(n)[::-1]) and bin(n)[2:] == bin(n)[2:][::-1]])
