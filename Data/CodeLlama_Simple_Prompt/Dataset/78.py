def hex_key(num):
    prime_digits = set([2, 3, 5, 7, 11, 13])
    num = num.upper()
    count = 0
    for char in num:
        if char in prime_digits:
            count += 1
    return count
