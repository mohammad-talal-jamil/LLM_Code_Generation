def sort_even(l):
    l_copy = l.copy()
    for i in range(0, len(l), 2):
        l_copy[i] = sorted(l[i::2])
    return l_copy
