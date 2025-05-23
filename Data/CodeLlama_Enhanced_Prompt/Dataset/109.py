def move_one_ball(arr):
    """
    We have an array 'arr' of N integers arr[1], arr[2], ..., arr[N]. The numbers in the array will be randomly ordered. Your task is to determine if it is possible to get an array sorted in non-decreasing order by performing the following operation on the given array:

    You are allowed to perform right shift operation any number of times.

    One right shift operation means shifting all elements of the array by one position in the right direction. The last element of the array will be moved to the starting position in the array i.e. 0th index.

    If it is possible to obtain the sorted array by performing the above operation then return True else return False.
    If the given array is empty then return True.

    Note: The given list is guaranteed to have unique elements.
    """
    if len(arr) == 0:
        return True
    min_value = min(arr)
    min_index = arr.index(min_value)
    my_arr = arr[min_index:] + arr[:min_index]
    for i in range(len(arr)):
        if my_arr[i] != sorted(arr)[i]:
            return False
    return True
