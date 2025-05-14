def fib4(n: int) -> int:
    if n <= 3:
        return 0
    if n == 4:
        return 2

    seq = [0, 0, 2, 0]
    for i in range(4, n+1):
        seq.append(seq[i-1] + seq[i-2] + seq[i-3] + seq[i-4])

    return seq[n]
