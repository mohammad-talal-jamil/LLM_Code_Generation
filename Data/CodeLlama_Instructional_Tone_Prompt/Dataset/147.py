def get_max_triples(n):
    # create an integer array a of length n
    a = [i * i - i + 1 for i in range(1, n + 1)]
    count = 0
    # iterate over each element in the array
    for i in range(len(a)):
        # check if the current element is a multiple of 3
        if a[i] % 3 == 0:
            # iterate over the remaining elements to find pairs that add up to the current element
            for j in range(i + 1, len(a)):
                if (a[j] + a[i]) % 3 == 0:
                    count += 1
    return count
