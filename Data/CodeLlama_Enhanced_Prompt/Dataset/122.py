def add_elements(arr, k):
    return sum(map(int, map(str.strip, arr[:k])))
