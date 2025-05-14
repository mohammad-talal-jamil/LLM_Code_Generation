def prod_signs(arr):
    if not arr:
        return None
    sum = 0
    sign = 1
    for num in arr:
        sum += abs(num) * sign
        sign *= (num > 0) - (num < 0)
    return sum
