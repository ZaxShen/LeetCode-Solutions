# Last updated: 8/17/2025, 4:40:22 PM
from collections import defaultdict

class Solution:
	# O(n*mlogm), O(n*m)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        for s in strs:
            # Sort characters to create canonical anagram form
            key = ''.join(sorted(s))  # O(m*mlogm)
            groups[key].append(s)
        
        return list(groups.values())