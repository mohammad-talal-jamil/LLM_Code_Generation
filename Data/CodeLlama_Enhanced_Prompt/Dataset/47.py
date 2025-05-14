def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    8.0
    """
    n = len(l) // 2
    if n % 2 == 1:
        return l[n]
    else:
        return (l[n - 1] + l[n]) / 2.0
