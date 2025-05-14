def find_zero(xs: list):
    """
    Finds a zero point of a polynomial with coefficients xs.

    Args:
        xs: List of polynomial coefficients.

    Returns:
        Zero point of the polynomial.
    """
    import math

    # Initialize variables
    begin, end = -1., 1.
    middle = (begin + end) / 2.0
    multiplier = 2.0

    # Iterate until the zero point is found
    while poly(xs, middle) * poly(xs, begin) > 0:
        begin *= multiplier
        end *= multiplier
        middle = (begin + end) / 2.0

    # Return the zero point
    return middle
