def next_smallest(lst):
    if len(lst) == 0:
        return None
    smallest = min(lst)
    second_smallest = None
    for i in lst:
        if i < smallest and i != second_smallest:
            second_smallest = i
    return second_smallest
