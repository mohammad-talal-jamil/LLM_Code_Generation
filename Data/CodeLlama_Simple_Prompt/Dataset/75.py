def is_multiply_prime(a):
    if a < 1:
        return False
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0 and (a / i < i or not is_multiply_prime(a / i)):
            return True
    return False
