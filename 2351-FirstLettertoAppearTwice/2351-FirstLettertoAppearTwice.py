# Last updated: 8/16/2025, 12:41:49 PM
from collections import Counter

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        counter = Counter()

        for char in s:
            counter[char] += 1
            if counter[char] == 2:
                return char

        