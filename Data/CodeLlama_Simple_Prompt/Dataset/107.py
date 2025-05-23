def even_odd_palindrome(n):
    even_count = 0
    odd_count = 0
    for i in range(1, n+1):
        if is_palindrome(i):
            if is_even(i):
                even_count += 1
            else:
                odd_count += 1
    return (even_count, odd_count)


def is_palindrome(num):
    return str(num) == str(num)[::-1]


def is_even(num):
    return num % 2 == 0
