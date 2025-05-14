def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    """
    # sort the array in ascending order
    nums.sort()
    # initialize the minimum sum to the first element
    min_sum = nums[0]
    # loop through the array and update the minimum sum
    for i in range(1, len(nums)):
        if nums[i] < min_sum:
            min_sum = nums[i]
    return min_sum
