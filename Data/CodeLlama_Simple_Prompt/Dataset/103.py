def rounded_avg(n, m):
    if n > m:
        return -1
    return bin(int((n + m) / 2))[2:]
