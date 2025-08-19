class Solution:
    # O(n), O(k)
    def repeatedCharacter(self, s: str) -> str:
        counter = {}

        for char in s:
            # Early termination
            if char in counter:
                return char
            counter[char] = counter.get(char, 0) + 1
