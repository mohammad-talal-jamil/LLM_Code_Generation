def rounded_avg(n, m):
    if n > m:
        return -1
    total = 0
    for i in range(n, m + 1):
        total += i
    average = int(total / (m - n + 1))
    binary_string = bin(average)[2:]
    return "0b" + binary_string
