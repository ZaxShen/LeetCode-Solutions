# Last updated: 8/14/2025, 1:16:55 AM
from collections import Counter

class Solution:
    # O(n), O(n)
    def repeatedCharacter(self, s: str) -> str:
        counter = Counter()

        for char in s:
            counter[char] += 1
            if counter[char] == 2:
                return char