# Last updated: 8/13/2025, 7:41:18 PM
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        count = res = sum(char in vowels for char in s[:k])

        for i in range(k, len(s)):
            count += (s[i] in vowels) - (s[i - k] in vowels)
            res = max(res, count)

        return res