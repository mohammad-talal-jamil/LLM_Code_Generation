def digit_sum(s):
    return sum(ord(char) for char in s if char.isupper())
