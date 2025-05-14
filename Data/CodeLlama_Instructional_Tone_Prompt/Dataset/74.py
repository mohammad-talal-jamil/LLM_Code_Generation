def total_match(lst1, lst2):
    if len("".join(lst1)) <= len("".join(lst2)):
        return lst1
    else:
        return lst2
