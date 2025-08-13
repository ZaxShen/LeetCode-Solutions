# Last updated: 8/13/2025, 1:35:27 PM
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')

        # First window
        count = res = sum(char in vowels for char in s[:k])

        # Sliding window
        for i in range(k, len(s)):
            if res == k:
                return res
            if s[i] in vowels:
                count += 1
            if s[i - k] in vowels:
                count -= 1
            res = max(res, count)

        return res