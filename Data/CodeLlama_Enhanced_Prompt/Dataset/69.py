def search(lst):
    # frequency of each element
    freq = {}
    for i in lst:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    # find the element with maximum frequency
    max_freq = -1
    max_freq_elem = None
    for elem, freq in freq.items():
        if freq > max_freq:
            max_freq = freq
            max_freq_elem = elem

    # check if the element with maximum frequency is greater than or equal to the value of the element itself
    if max_freq_elem and max_freq_elem >= max_freq:
        return max_freq_elem
    else:
        return -1
