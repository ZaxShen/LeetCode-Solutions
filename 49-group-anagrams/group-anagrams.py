from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for s in strs:
            key = tuple(sorted(s))
            hashmap[key].append(s)

        return list(hashmap.values())