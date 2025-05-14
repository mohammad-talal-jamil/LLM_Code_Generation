def fib4(n):
    if n <= 3:
        return 0
    elif n == 4:
        return 2
    a, b, c, d = 0, 0, 2, 0
    for i in range(5, n + 1):
        a, b, c, d = b, c, d, a + b + c + d
    return d
