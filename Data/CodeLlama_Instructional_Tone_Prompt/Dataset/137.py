def compare_one(a, b):
    if type(a) != type(b):
        raise TypeError("Cannot compare different types")
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return None
