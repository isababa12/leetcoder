def trafficJam(t, grid):
    step = t
    new_grid = grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 2:
                if j+1 < len(grid[i]) and grid[i][j+1] == 1:
                    new_grid[i][j+1] = 2
                if j-1 >= 0 and grid[i][j-1] == 1:
                    new_grid[i][j-1] = 2
                if i+1 < len(grid) and grid[i+1][j] == 1:
                    new_grid[i+1][j] = 2
                if i-1 >= 0 and grid[i-1][j] == 1:
                    new_grid[i-1][j] = 2
            if 1 in new_grid:
                step += 1
                return trafficJam(step, grid = new_grid)
            return t

print("t:", trafficJam(0, [[2, 2, 1, 1],
                            [2, 2, 0, 1],
                            [0, 2, 0, 2],
                            [0, 1, 2, 1]]))
