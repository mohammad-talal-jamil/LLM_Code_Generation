def is_sorted(lst):
    return all(lst[i-1] <= lst[i] for i in range(1, len(lst)))
