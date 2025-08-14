# Last updated: 8/14/2025, 1:15:44 AM
from collections import Counter

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        counter = Counter()

        for i, char in enumerate(s):
            counter[char] += 1
            if counter[char] == 2:
                return char