def get_row(lst, x):
    coords = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == x:
                coords.append((i, j))
    return sorted(coords, key=lambda x: (x[0], -x[1]))
