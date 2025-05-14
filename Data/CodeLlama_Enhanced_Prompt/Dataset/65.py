def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    """
    # convert x to string
    s = str(x)
    # get length of string
    n = len(s)
    # if shift is greater than number of digits
    if shift > n:
        # reverse the string
        return s[::-1]
    else:
        # circular shift the digits by shift amount
        return s[n-shift:] + s[:n-shift]
