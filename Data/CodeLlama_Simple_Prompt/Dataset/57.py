def monotonic(l):
    if len(l) <= 1:
        return True
    return all(l[i] >= l[i-1] for i in range(1, len(l))) or all(l[i] <= l[i-1] for i in range(1, len(l)))
