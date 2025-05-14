def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        for j, column in enumerate(row):
            if column == x:
                result.append((i, j))
    return sorted(result)
