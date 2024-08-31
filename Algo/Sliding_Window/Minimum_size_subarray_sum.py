'''
Given an array of positive integers nums and a positive integer target,
return the minimal length of a subarray whose sum is greater than or equal to target.
If there is no such subarray, return 0 instead.
'''


def minSubArrayLen(target, nums):
    """
    :type target: int
    :type nums: List[int]
    :rtype: int
    """
    val_sum = 0
    times = float('inf')
    end = 0
    for i in range(len(nums)):
        val_sum += nums[i]
        while val_sum >= target:
            times = min(times, i + 1 - end)
            val_sum -= nums[end]
            end += 1

    return times if times != float('inf') else 0

print(minSubArrayLen(22,[12,3,1,2,4,10]))