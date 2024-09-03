def majorityElement(nums) -> int:
    nums.sort()
    n = len(nums)
    return nums[n // 2]
print(majorityElement([2,2,1,1,1,2,2]))