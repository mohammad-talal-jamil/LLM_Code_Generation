def circular_shift(x, shift):
    # convert integer to string
    str_x = str(x)
    # get the number of digits in the string
    num_digits = len(str_x)
    # if shift is greater than the number of digits, reverse the string
    if shift > num_digits:
        return str_x[::-1]
    # otherwise, rotate the string by shift digits
    else:
        return str_x[num_digits-shift:] + str_x[:num_digits-shift]
