def f(n):
    factorial = 1
    for i in range(1, n+1):
        if i % 2 == 0:
            factorial *= i
            result.append(factorial)
        else:
            result.append(sum(range(1, i+1)))
    return result
