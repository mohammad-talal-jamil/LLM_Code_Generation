def double_the_difference(lst):
    """
    Given a list of numbers, return the sum of squares of the numbers in the list that are odd. Ignore numbers that are negative or not integers.
    """
    # Initialize the sum to 0
    sum = 0
    # Iterate over the list
    for num in lst:
        # Check if the number is odd and positive
        if num % 2 != 0 and num > 0:
            # Add the square of the number to the sum
            sum += num ** 2
    # Return the sum
    return sum
