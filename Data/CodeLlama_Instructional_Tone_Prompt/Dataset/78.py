def hex_key(num):
    prime_digits = [2, 3, 5, 7, 11, 13]
    count = 0
    for char in num:
        if char in "0123456789":
            if int(char) in prime_digits:
                count += 1
        elif char in "ABCDEF":
            if int(char, 16) in prime_digits:
                count += 1
    return count
