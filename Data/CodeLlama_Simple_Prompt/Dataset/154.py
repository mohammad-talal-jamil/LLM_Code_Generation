def cycpattern_check(a, b):
    return b in a or any(b in a[i:] for i in range(len(a)))
