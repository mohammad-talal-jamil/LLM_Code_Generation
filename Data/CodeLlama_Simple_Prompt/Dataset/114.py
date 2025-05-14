def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # use a variable to store the minimum sum
    min_sum = float('inf')
    # loop over the array
    for i in range(len(nums)):
        # use a variable to store the current sum
        current_sum = 0
        # loop over the sub-array starting at index i
        for j in range(i, len(nums)):
            # add the current element to the current sum
            current_sum += nums[j]
            # update the minimum sum if necessary
            min_sum = min(min_sum, current_sum)
    # return the minimum sum
    return min_sum
