# Last updated: 8/15/2025, 5:01:38 PM
class Solution:
    # O(n), O(1)
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')

        # First window
        res = count = sum(char in vowels for char in s[:k])

        # Sliding window
        for i in range(k, len(s)):
            count += (s[i] in vowels) - (s[i - k] in vowels)
            res = max(res, count)
            # Optional: early termination for O(k) in best case
            if res == k:
                return res

        return res