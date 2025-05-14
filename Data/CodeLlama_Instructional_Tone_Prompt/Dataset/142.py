def sum_squares(lst):
    result = 0
    for i, x in enumerate(lst):
        if i % 3 == 0:
            result += x * x
        elif i % 4 == 0:
            result += x * x * x
        else:
            result += x
    return result
