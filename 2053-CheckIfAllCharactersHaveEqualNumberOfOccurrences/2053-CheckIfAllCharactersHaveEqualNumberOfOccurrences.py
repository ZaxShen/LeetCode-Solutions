# Last updated: 8/4/2025, 10:43:54 PM
from collections import defaultdict

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts = defaultdict(int)

        for i in s:
            counts[i] += 1

        uni = set(counts.values())

        if len(uni) == 1:
            return True

        return False