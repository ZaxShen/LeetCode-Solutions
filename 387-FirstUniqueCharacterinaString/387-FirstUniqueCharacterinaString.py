# Last updated: 8/13/2025, 10:27:17 AM
from collections import Counter

class Solution:
    # O(n), O(n)
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        
        for i, char in enumerate(s):
            if counter[char] == 1:
                return i

        return -1