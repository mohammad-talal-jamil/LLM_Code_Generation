def add(lst):
    result = 0
    for i in range(1, len(lst), 2):
        result += lst[i]
    return result
