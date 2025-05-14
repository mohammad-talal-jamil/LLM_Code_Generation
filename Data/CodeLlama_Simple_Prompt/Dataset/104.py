def unique_digits(x):
    """
    Given a list of positive integers, return a sorted list of all elements that haven't any even digit.
    Note: Returned list should be sorted in increasing order.
    """
    def has_even_digit(n):
        while n > 0:
            if n % 2 == 0:
                return True
            n //= 10
        return False
    return sorted([i for i in x if not has_even_digit(i)])
