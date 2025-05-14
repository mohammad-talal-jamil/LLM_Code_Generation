def sort_third(l):
    l[::3] = sorted(l[::3])
    return l
