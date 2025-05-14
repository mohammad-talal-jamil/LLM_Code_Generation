def search(lst):
    # frequency of each element is stored in a dictionary
    freq = {}
    for i in lst:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    # find the maximum value in the frequency dictionary
    max_value = max(freq.values())

    # check if there is any element with a frequency greater than or equal to its value
    for i in freq:
        if freq[i] >= i and i > 0:
            return i

    return -1
