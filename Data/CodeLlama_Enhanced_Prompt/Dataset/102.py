def choose_num(x, y):
    """
    This function takes two positive numbers x and y and returns the biggest even integer number that is in the range [x, y] inclusive. If there's no such number, then the function should return -1.
    """
    # Check if x is greater than y
    if x > y:
        return -1

    # Check if y is even
    if y % 2 == 0:
        return y

    # Check if x is equal to y
    if x == y:
        return -1

    # Return the largest even number in the range [x, y]
    return y - 1
