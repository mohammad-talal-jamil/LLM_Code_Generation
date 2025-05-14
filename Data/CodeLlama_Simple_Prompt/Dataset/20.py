from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Find and return the two closest elements in a given list of numbers.

    Args:
        numbers (List[float]): A list of numbers of length at least two.

    Returns:
        Tuple[float, float]: The two closest elements in the list, in order from smallest to largest.
    """
    # Sort the list in ascending order
    numbers.sort()

    # Initialize the closest elements and their difference
    closest_elements = (numbers[0], numbers[1])
    closest_diff = closest_elements[1] - closest_elements[0]

    # Iterate over the list, starting from the third element
    for i in range(2, len(numbers)):
        # Calculate the difference between the current element and its predecessor
        current_diff = numbers[i] - numbers[i-1]

        # Check if the current difference is smaller than the closest difference
        if current_diff < closest_diff:
            # Update the closest elements and their difference
            closest_elements = (numbers[i-1], numbers[i])
            closest_diff = current_diff

    return closest_elements
