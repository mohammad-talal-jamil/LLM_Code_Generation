def largest_prime_factor(n):
    for i in range(int(n**0.5), 1, -1):
        if n % i == 0 and is_prime(i):
            return i
    return 1


def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
