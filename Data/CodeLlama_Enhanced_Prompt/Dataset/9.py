def rolling_max(numbers: List[int]) -> List[int]:
    result = []
    for n in numbers:
        if not result or result[-1] < n:
            result.append(n)
        else:
            result.append(result[-1])
    return result
