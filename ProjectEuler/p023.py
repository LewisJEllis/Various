def is_abundant(n):
    return sum([i for i in range(1,n/2+1) if n % i == 0]) > n

abundants = [i for i in range(12, 2812) if is_abundant(i)]
# too slow, need to generate these treelike rather than listlike
print abundants
#def sum_of_two(n):
#    return true/false

#print sum([i for i in range(21824) if not sum_of_two())