goal = 347991

# Part 1
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def spiral(goal):
    pos = (0,0)
    data = 1
    inc = 2
    while True:
        for d in dirs:
            dx,dy = d
            for i in range(inc//2):
                data += 1
                pos = (pos[0] + dx, pos[1] + dy)
                if data == goal:
                    return pos
            inc += 1

dest = spiral(goal)
print('Part 1: ', abs(dest[0]) + abs(dest[1]))

# Part 2
def neighbor_total(grid, pos):
    x,y = pos
    return (grid[x-1][y-1] + grid[x][y-1] + grid[x+1][y-1] + grid[x-1][y] +
        grid[x+1][y] + grid[x-1][y+1] + grid[x][y+1] + grid[x+1][y+1])

# Dirs are different than above because Part 2's code indexes into a list
# representation of the grid instead of tracking a Cartesian coordinate for the
# current position.
dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
def spiral_total(grid, goal, start):
    pos = start
    inc = 2
    while True:
        for d in dirs:
            dx,dy = d
            for i in range(inc//2):
                pos = (pos[0] + dx, pos[1] + dy)
                data = neighbor_total(grid, pos)
                grid[pos[0]][pos[1]] = data
                if data > goal:
                    return data
            inc += 1

n = 11
grid = [[0 for i in range(n)] for j in range(n)]
mid = n//2
grid[mid][mid] = 1
print('Part 2: ', spiral_total(grid, goal, (mid, mid)))
