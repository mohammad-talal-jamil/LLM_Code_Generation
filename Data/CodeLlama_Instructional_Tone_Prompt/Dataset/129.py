def minPath(grid, k):
    def find_min_path(cur_row, cur_col, cur_path, remaining):
        if remaining == 0:
            return cur_path
        next_row = cur_row + 1
        next_col = cur_col + 1
        if next_row >= len(grid) or next_col >= len(grid[0]):
            return None
        next_cell = grid[next_row][next_col]
        if next_cell in cur_path:
            return None
        result = find_min_path(
            next_row, next_col, cur_path + [next_cell], remaining - 1)
        if result is not None:
            return result
        else:
            return find_min_path(cur_row, cur_col, cur_path, remaining)

    min_path = []
    for i in range(k):
        min_path.append(1)
    return find_min_path(0, 0, min_path, k)
