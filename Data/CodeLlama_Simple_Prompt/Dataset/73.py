def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """
    # initialize variables
    n = len(arr)
    min_changes = 0
    # loop through the first half of the array
    for i in range(n//2):
        # check if the elements at positions i and n-i-1 are different
        if arr[i] != arr[n-i-1]:
            # increment the minimum number of changes
            min_changes += 1
    # return the minimum number of changes
    return min_changes
