def get_largest_prime_sum_digits(my_list):
    # find the largest prime number in the list
    largest_prime = 0
    for num in my_list:
        if is_prime(num) and num > largest_prime:
            largest_prime = num
    # return the sum of its digits
    return sum(int(digit) for digit in str(largest_prime))


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
