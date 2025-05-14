def total_match(lst1, lst2):
    return sorted(lst1, key=len)[0] if sum(len(s) for s in lst1) <= sum(len(s) for s in lst2) else sorted(lst2, key=len)[0]
