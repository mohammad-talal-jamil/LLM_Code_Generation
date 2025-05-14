def special_factorial(n):
    """
    The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0
    """
    if n == 0:
        return 1
    else:
        return n * special_factorial(n-1)
