# Last updated: 8/16/2025, 7:11:09 PM
from collections import Counter

class Solution:
    # O(n), O(n)
    def areOccurrencesEqual(self, s: str) -> bool:
        return len(set(Counter(s).values())) == 1