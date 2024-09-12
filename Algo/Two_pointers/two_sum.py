def twoSum(numbers, target: int):
    left = 0
    right = len(numbers) - 1

    while left < right:
        total = numbers[left] + numbers[right]

        if total == target:
            return [left + 1, right + 1]
        elif total > target:
            right -= 1
        else:
            left += 1

    return []
print(twoSum([2,7,11,15],9))