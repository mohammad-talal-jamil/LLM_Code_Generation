def intersection(interval1, interval2):
    """
    Determine if the length of the intersection of two intervals is a prime number.

    Args:
        interval1 (tuple): The first interval.
        interval2 (tuple): The second interval.

    Returns:
        str: "YES" if the length of the intersection is a prime number, otherwise "NO".
    """
    # Sort intervals by start time
    sorted_intervals = sorted([interval1, interval2], key=lambda x: x[0])

    # Get the overlap between the two intervals
    overlap = sorted_intervals[1][0] - sorted_intervals[0][1]

    # Check if the overlap is a prime number
    if overlap > 1 and is_prime(overlap):
        return "YES"
    else:
        return "NO"


def is_prime(num):
    """
    Determine if a number is prime.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, otherwise False.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
