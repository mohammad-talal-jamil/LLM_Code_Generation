def fizz_buzz(n):
    count = 0
    for i in range(1, n+1):
        if i % 11 == 0 or i % 13 == 0:
            if str(i).count('7') > 0:
                count += 1
    return count
