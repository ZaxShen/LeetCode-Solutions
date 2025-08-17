# Last updated: 8/17/2025, 4:21:09 PM
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for s in strs:
            hashmap[''.join(sorted(s))].append(s)

        return list(hashmap.values())