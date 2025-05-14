def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Find and return the closest two elements from the list of numbers.
    The order of the output tuple is not important.
    If there are multiple pairs with the same minimum distance,
    return the first pair that was found in the list.
    """
    # Sort the list to enable finding the closest pair efficiently
    numbers.sort()
    # Initialize the smallest distance found and its corresponding pair
    smallest_distance = float('inf')
    closest_pair = ()

    # Iterate over the sorted list, starting from the second element
    for i in range(1, len(numbers)):
        # Calculate the distance between the current element and its previous one
        distance = numbers[i] - numbers[i-1]
        # If the distance is smaller than the smallest distance found, update the closest pair and the smallest distance
        if distance < smallest_distance:
            smallest_distance = distance
            closest_pair = (numbers[i-1], numbers[i])

    return closest_pair
