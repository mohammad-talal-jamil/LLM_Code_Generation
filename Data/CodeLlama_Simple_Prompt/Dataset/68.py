def pluck(arr):
    """
    Given an array representing a branch of a tree, return the value of the node with the smallest even value.
    If multiple nodes have the same smallest even value, return the node with the smallest index.
    If there are no even values or the given array is empty, return None.
    """
    # Edge case: if the input array is empty, return None
    if not arr:
        return None

    # Initialize variables to keep track of the smallest even value and its index
    smallest_even_value = None
    smallest_index = None

    # Loop through the input array
    for i in range(len(arr)):
        # Check if the current value is even
        if arr[i] % 2 == 0:
            # If we haven't found a smallest even value yet, set it to the current value and its index
            if smallest_even_value is None:
                smallest_even_value = arr[i]
                smallest_index = i
            # Compare the current value to the smallest even value
            elif arr[i] < smallest_even_value:
                smallest_even_value = arr[i]
                smallest_index = i

    # Return the value and index of the node with the smallest even value
    if smallest_even_value is not None:
        return [smallest_even_value, smallest_index]
    else:
        return None