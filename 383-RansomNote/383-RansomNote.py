# Last updated: 8/17/2025, 8:05:14 PM
from collections import Counter

class Solution:
    # O(n+m), O(n+m)
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not (Counter(ransomNote) - Counter(magazine))