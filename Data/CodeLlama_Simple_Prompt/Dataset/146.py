def specialFilter(nums):
    count = 0
    for num in nums:
        if num > 10 and num % 10 in [1, 3, 5, 7, 9] and num // 10 in [1, 3, 5, 7, 9]:
            count += 1
    return count
