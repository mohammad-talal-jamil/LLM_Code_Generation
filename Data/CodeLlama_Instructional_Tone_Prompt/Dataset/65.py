def circular_shift(x, shift):
    # convert x to a string
    s = str(x)
    # get the length of the string
    n = len(s)
    # compute the shift modulo the length of the string
    shift = shift % n
    # return the concatenation of the two slices of the string
    return s[n-shift:] + s[:n-shift]
