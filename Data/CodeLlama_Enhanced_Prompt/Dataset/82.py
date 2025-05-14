def prime_length(string):
    if not string:
        return False
    for i in range(2, len(string)):
        if len(string) % i == 0:
            return False
    return True
