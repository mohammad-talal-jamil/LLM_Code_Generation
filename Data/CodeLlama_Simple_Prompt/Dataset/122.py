def add_elements(arr, k):
    # sort the array in ascending order
    arr.sort()
    # initialize the sum to 0
    sum = 0
    # loop through the first k elements of the array
    for i in range(k):
        # extract the digits of the current element
        digits = [int(digit) for digit in str(arr[i])]
        # check if the number of digits is at most 2
        if len(digits) <= 2:
            # add the current element to the sum
            sum += arr[i]
    # return the sum
    return sum
