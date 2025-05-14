def by_length(arr):
    numbers = ["One", "Two", "Three", "Four",
               "Five", "Six", "Seven", "Eight", "Nine"]
    result = []
    for num in arr:
        if num >= 1 and num <= 9:
            result.append(numbers[num - 1])
    return result[::-1]
