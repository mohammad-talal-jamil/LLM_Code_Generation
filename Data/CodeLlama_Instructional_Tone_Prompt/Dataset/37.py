def sort_even(l):
    even_indices = range(0, len(l), 2)
    even_values = [l[i] for i in even_indices]
    even_values.sort()
    for i in range(len(even_indices)):
        l[even_indices[i]] = even_values[i]
    return l
