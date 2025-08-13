# Last updated: 8/13/2025, 1:38:32 PM
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')

        # First window
        count = res = sum(char in vowels for char in s[:k])

        # Sliding window
        for i in range(k, len(s)):
            count += (s[i] in vowels) - (s[i - k] in vowels)
            res = max(res, count)

        return res