def prod_signs(arr):
    if not arr:
        return None
    prod = 1
    sum = 0
    for num in arr:
        prod *= 1 if num > 0 else -1
        sum += abs(num)
    return prod * sum
