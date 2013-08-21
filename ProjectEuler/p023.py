# this is slow, i should generate these with a factoring tree instead
def is_abundant(n):
    return sum([i for i in range(1, n/2+1) if n % i == 0]) > n

lower = 12
upper = 20161
abundants = [i for i in range(lower, upper+1) if is_abundant(i)]
abundants_set = set(abundants)

def sum_of_two(n):
    for a in abundants:
        if a > n - lower:
            break
        if n - a in abundants_set:
            return True
    return False

print sum([i for i in range(1, upper+1) if not sum_of_two(i)])