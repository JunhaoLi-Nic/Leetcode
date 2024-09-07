def twoSum(nums, target: int):
    dic = {}

    for num in range(len(nums)):
        dic[nums[num]] = num

    for i in range(len(nums)):
        rest = target - nums[i]
        if rest in dic and dic[rest] != i:
            return[i,dic[rest]]
        return []

print(twoSum([2,7,11,15],9))