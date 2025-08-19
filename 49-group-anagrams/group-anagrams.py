from collections import defaultdict, Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for s in strs:
            key = tuple(sorted(Counter(s).items()))
            hashmap[key].append(s)

        return list(hashmap.values())