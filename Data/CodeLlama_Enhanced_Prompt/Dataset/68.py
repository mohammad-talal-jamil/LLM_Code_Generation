def pluck(arr):
    """
    Given an array representing a branch of a tree that has non-negative integer nodes,
    your task is to pluck one of the nodes and return it. The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value are found, return the node that has the smallest index.
    The plucked node should be returned in a list, [smallest_value, its_index], if there are no even values or the given array is empty, return [].
    """
    if not arr:
        return []
    evens = [x for x in arr if x % 2 == 0]
    if not evens:
        return []
    smallest_even = min(evens)
    index = arr.index(smallest_even)
    return [smallest_even, index]
