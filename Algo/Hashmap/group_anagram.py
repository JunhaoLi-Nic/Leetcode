from collections import defaultdict
def groupAnagrams(strs):
    ans = defaultdict(list)

    for s in strs:
        key = "".join(sorted(s))
        ans[key].append(s)

    return ans.values()

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))