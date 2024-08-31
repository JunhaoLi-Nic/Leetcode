
def summaryRanges(nums):
    ranges = [] # [start, end] or [x, y]
    for n in nums:
        if ranges and ranges[-1][1] == n-1:
            ranges[-1][1] = n
        else:
            ranges.append([n, n])

    return [f'{x}->{y}' if x != y else f'{x}' for x, y in ranges]

nums = [0,1,2,4,5,7]
print(summaryRanges(nums))