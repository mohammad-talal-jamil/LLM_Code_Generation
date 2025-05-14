def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    fib_seq = [0, 1]
    while len(fib_seq) <= n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    for i in range(len(fib_seq)):
        if is_prime(fib_seq[i]):
            return fib_seq[i]


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
