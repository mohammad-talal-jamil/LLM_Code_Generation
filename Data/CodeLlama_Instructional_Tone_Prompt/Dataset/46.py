def fib4(n: int) -> int:
    if n <= 3:
        return 0
    elif n == 4:
        return 2

    dp = [0] * (n + 1)
    dp[0], dp[1], dp[2], dp[3] = 0, 0, 2, 0

    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4]

    return dp[n]
