# Last updated: 8/16/2025, 12:43:13 PM
from collections import Counter

class Solution:
    # O
    def repeatedCharacter(self, s: str) -> str:
        hashset = set()

        for char in s:
            if char in hashset:
                return char
            hashset.add(char)

        