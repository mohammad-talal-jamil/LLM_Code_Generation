def is_multiply_prime(a):
    for i in range(2, 101):
        if a % i == 0:
            for j in range(2, 101):
                if a % j == 0:
                    for k in range(2, 101):
                        if a == i * j * k:
                            return True
    return False
