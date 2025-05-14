def search(lst):
    # create a dictionary to store the count of each integer
    freq = {}
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # sort the dictionary by key in descending order
    sorted_freq = sorted(freq.items(), key=lambda x: x[0], reverse=True)

    # loop through the sorted dictionary and find the first integer that meets the condition
    for num, count in sorted_freq:
        if count >= num:
            return num
    return -1
