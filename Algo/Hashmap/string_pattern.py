def wordPattern(pattern: str, s: str) -> bool:
    map1 = []
    map2 = []
    s = s.split()
    if len(pattern) != len(s):
        return False

    for i in s:
        map1.append(s.index(i))

    for char in pattern:
        map2.append(pattern.index(char))

    if map1 == map2:
        return True

    return False

print(wordPattern("abba","dog cat cat dog"))