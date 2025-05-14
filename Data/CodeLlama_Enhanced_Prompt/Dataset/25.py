def factorize(n: int) -> List[int]:
    if n == 1:
        return [1]

    factors = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            factors.extend(factorize(n//i))
            break

    return factors or [n]
