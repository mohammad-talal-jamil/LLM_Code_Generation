def tri(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 3]
    else:
        result = [1, 3]
        for i in range(2, n):
            if i % 2 == 0:
                result.append(result[i - 1] + (i / 2))
            else:
                result.append(result[i - 2] + result[i - 1] + result[i + 1])
        return result
