def canJump(nums) -> bool:
    gas = 0
    for n in nums:
        if gas < 0:
            return False
        elif n > gas:
            gas = n
        gas -= 1

    return True
print(canJump([3,0,8,2,0,0,1]))