from collections import defaultdict


def isAnagram(s: str, t: str) -> bool:
    count = defaultdict(int)
    if len(s) != len(t):
        return False
    for char in s:
        count[char] +=1
    for char in t:
        count[char] -=1
    for val in count.values():
        if val != 0:
            return False
    return True

print(isAnagram('anagram','nagaram'))