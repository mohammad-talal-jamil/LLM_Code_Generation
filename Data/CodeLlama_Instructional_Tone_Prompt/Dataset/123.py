def get_odd_collatz(n):
    def generate_sequence(n):
        if n == 1:
            return [1]
        else:
            if n % 2 == 0:
                return [n] + generate_sequence(n // 2)
            else:
                return [n] + generate_sequence(3 * n + 1)

    sequence = generate_sequence(n)
    return sorted([x for x in sequence if x % 2 == 1])
