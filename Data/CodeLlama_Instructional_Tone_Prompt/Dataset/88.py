def sort_array(array):
    sum_first_last = array[0] + array[-1]
    if sum_first_last % 2 == 1:
        return sorted(array)
    else:
        return sorted(array, reverse=True)
