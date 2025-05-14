def sort_numbers(numbers: str) -> str:
    numbers = numbers.split(' ')
    value_map = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
                 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    numbers.sort(key=lambda x: value_map[x])
    return ' '.join(numbers)
