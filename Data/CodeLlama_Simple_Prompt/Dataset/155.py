def even_odd_count(num):
    """Given an integer, return a tuple that has the number of even and odd digits respectively.

        Example:
            even_odd_count(-12) ==> (1, 1)
            even_odd_count(123) ==> (1, 2)
    """
    str_num = str(abs(num))
    count_even = 0
    count_odd = 0
    for char in str_num:
        if int(char) % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    return (count_even, count_odd)
