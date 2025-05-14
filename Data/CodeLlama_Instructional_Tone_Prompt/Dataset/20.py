def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Find the closest two elements in a list of numbers and return them in order.
    If there are multiple pairs with the same minimum distance, return the pair with the largest elements.
    """
    # Sort the list to make it easier to find the closest elements
    numbers.sort()
    closest_pair = (numbers[0], numbers[1])
    minimum_distance = numbers[1] - numbers[0]

    # Iterate over the list and find the closest pair
    for i in range(len(numbers) - 1):
        distance = numbers[i + 1] - numbers[i]
        if distance < minimum_distance:
            closest_pair = (numbers[i], numbers[i + 1])
            minimum_distance = distance

    return closest_pair
