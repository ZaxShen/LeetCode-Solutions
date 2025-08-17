# Last updated: 8/17/2025, 4:27:32 PM
from collections import defaultdict

class Solution:
    # O(n*m*mlogm), O(n*m)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))
            hashmap[key].append(s)

        return list(hashmap.values())