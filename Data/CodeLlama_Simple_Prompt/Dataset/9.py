from typing import List


def rolling_max(numbers: List[int]) -> List[int]:
    max_until_index = [0] * len(numbers)
    for i in range(len(numbers)):
        max_until_index[i] = max(numbers[:i+1])
    return max_until_index
