# Last updated: 8/17/2025, 4:34:11 PM
from collections import defaultdict, Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        
        for s in strs:
            # Count character frequencies
            count = Counter(s)
            # Create hashable key from frequency
            key = tuple(sorted(count.items()))
            hashmap[key].append(s)
        
        return list(hashmap.values())