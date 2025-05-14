def below_threshold(numbers: list, threshold: int) -> bool:
    return all(n < threshold for n in numbers)
