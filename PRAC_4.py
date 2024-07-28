def specialArray(nums):
    nums.sort()
    n = len(nums)
    for x in range(n+1):
        pos = 0
        while pos < n and nums[pos] < x:
            pos += 1
        if n - pos == x:
            return x
    return -1
nums = [0,4,2,0]
print(specialArray(nums))