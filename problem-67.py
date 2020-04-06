## Problem 67
## Maximum path sum 2

from urllib2 import urlopen

connection = urlopen("https://projecteuler.net/project/resources/p067_triangle.txt")
data = connection.read()

grid = data.split("\n")
grid = [row.split(" ") for row in grid]
grid.pop()
grid = [[int(value) for value in row] for row in grid]

for i in reversed(range(len(grid) - 1)):
    for j in range(len(grid[i])):
        grid[i][j] = grid[i][j] + max(grid[i+1][j], grid[i+1][j+1])

print grid[0][0]
