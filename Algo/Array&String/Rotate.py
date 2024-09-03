def rotate(nums, k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k = k % len(nums)
    if k != 0:
        nums[:k], nums[k:] = nums[-k:], nums[:-k]
    return nums

print(rotate([1,2,3,4,5,6,7],3))