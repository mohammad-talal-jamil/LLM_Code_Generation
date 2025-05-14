def prime_fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        while b % 2 == 0 and b > 1:
            b //= 2
        if b <= 1:
            break
    return a
