# Last updated: 8/14/2025, 1:17:53 AM
class Solution:
    # O(n), O(n)
    def repeatedCharacter(self, s: str) -> str:
        uni_s = set()

        for char in s:
            if char in uni_s:
                return char
            uni_s.add(char)