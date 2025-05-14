def greatest_common_divisor(a, b):
    """
    Returns the greatest common divisor of two integers a and b
    """
    # Initialize the gcd to 0
    gcd = 0
    # Loop through all possible factors
    for i in range(1, min(a, b) + 1):
        # Check if both a and b are divisible by i
        if a % i == 0 and b % i == 0:
            # If they are, then i is a common divisor
            # and it is the greatest one so far
            gcd = i
    # Return the greatest common divisor
    return gcd
