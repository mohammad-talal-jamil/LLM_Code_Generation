def int_to_mini_roman(number):
    mini_roman = {
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm'
    }
    num_str = str(number)
    roman_str = ''
    for i in range(len(num_str)):
        digit = int(num_str[i])
        if digit == 9:
            roman_str += mini_roman[10**i] + mini_roman[5*10**i]
        elif digit >= 5:
            roman_str += mini_roman[5*10**i] + (digit-5)*mini_roman[10**i]
        else:
            roman_str += digit*mini_roman[10**i]
    return roman_str
