# Last updated: 8/13/2025, 10:17:29 AM
from collections import Counter

class Solution:

    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        key = min(counter, key=counter.get)

        return s.index(key) if counter[key] == 1 else -1