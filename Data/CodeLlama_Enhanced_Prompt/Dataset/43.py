def pairs_sum_to_zero(l):
    """
    Returns True if there are two distinct elements in the list that sum to zero, and False otherwise.
    """
    seen = set()
    for elem in l:
        if elem in seen:
            continue
        seen.add(elem)
        complement = -elem
        if complement in seen:
            return True
    return False
