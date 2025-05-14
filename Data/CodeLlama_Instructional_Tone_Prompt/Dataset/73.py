def smallest_change(arr):
    # Calculate the length of the array
    n = len(arr)

    # Initialize a 2D array to store the differences
    diff = [[0] * (n + 1) for _ in range(n + 1)]

    # Fill in the differences for the base cases
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if arr[i - 1] == j:
                diff[i][j] = diff[i - 1][j - 1]
            else:
                diff[i][j] = min(diff[i - 1][j - 1], diff[i - 1][j]) + 1

    # Return the minimum number of changes needed
    return diff[n][n]
