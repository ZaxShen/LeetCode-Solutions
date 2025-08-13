# Last updated: 8/13/2025, 10:25:01 AM
from collections import Counter

class Solution:
    # O(n), O(n)
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        
        for k, v in counter.items():
            if v == 1:
                return s.index(k)
        
        return -1