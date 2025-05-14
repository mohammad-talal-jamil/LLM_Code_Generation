def sort_third(l):
    return [val if i % 3 else sorted(val) for i, val in enumerate(l)]
