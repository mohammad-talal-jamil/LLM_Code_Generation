def unique_digits(x):
    return list(filter(lambda y: not any(int(c) % 2 == 0 for c in str(y)), sorted(x)))
