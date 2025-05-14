def largest_smallest_integers(lst):
    smallest = None
    largest = None
    for num in lst:
        if num < 0:
            if smallest is None or num > smallest:
                smallest = num
        elif num > 0:
            if largest is None or num < largest:
                largest = num
    return (smallest, largest)
