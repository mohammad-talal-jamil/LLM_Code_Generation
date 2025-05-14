from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given a list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    """
    smallest = min(numbers)
    largest = max(numbers)

    result = []
    for num in numbers:
        result.append((num - smallest) / (largest - smallest))

    return result
