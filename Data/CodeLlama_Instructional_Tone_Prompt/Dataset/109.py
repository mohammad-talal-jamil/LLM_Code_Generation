def move_one_ball(arr):
    # Check if the array is already sorted
    if arr == sorted(arr):
        return True

    # Check if it is possible to sort the array by right shifting elements
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False

    return True
