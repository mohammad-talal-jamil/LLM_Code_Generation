def hex_key(num):
    primes = set('2357BDF')
    return sum(c in primes for c in num)
