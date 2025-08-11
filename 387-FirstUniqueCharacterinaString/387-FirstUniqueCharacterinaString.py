# Last updated: 8/11/2025, 12:18:01 AM
from collections import Counter

class Solution:
    # O(n), O(n)
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        min_count = min(counter, key=counter.get)

        return s.index(min_count) if counter[min_count] == 1 else -1
