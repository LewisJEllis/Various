grid = map(lambda s: map(int, s.split(',')), open('p081matrix.txt', 'r').readlines())
l = len(grid)

# fill the left column and top row first
for i in range(1, l):
    grid[i][0] += grid[i-1][0]
    grid[0][i] += grid[0][i-1]

# then it's a simple dynamic programming problem
for i in range(1, l):
    for j in range(1, l):
        grid[i][j] += min(grid[i-1][j], grid[i][j-1])

print grid[-1][-1]