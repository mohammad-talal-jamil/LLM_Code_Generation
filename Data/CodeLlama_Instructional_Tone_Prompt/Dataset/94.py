def skjkasdkd(lst):
    prime_digits_sum = 0
    for i in lst:
        if is_prime(i):
            prime_digits_sum += sum(int(d) for d in str(i))
    return prime_digits_sum


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
