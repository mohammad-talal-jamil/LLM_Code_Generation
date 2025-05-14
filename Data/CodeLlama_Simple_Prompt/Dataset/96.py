def count_up_to(n):
    """
    Implement a function that takes an non-negative integer and returns an array of the first n integers that are prime numbers and less than n.
    """
    # Initialize an empty list to store the prime numbers
    prime_list = []
    # Loop through the numbers from 2 to n
    for num in range(2, n+1):
        # Check if the number is prime
        if is_prime(num):
            # If it is prime, add it to the list
            prime_list.append(num)
    # Return the list of prime numbers
    return prime_list


def is_prime(num):
    # Check if the number is divisible by any number between 2 and the square root of the number
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    # If the number is not divisible by any number between 2 and the square root of the number, it is prime
    return True
