def max_fill(grid, capacity):
    rows = len(grid)
    cols = len(grid[0])
    result = 0
    for i in range(rows):
        count = 0
        for j in range(cols):
            if grid[i][j] == 1:
                count += 1
        result += math.ceil(count / capacity)
    return result
