def choose_num(x, y):
    if x > y:
        x, y = y, x
    for i in range(y, x - 1, -1):
        if i % 2 == 0:
            return i
    return -1
