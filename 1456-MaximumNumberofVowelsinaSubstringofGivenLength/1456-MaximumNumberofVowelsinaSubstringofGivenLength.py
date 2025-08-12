# Last updated: 8/12/2025, 7:02:54 PM
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')

        count = sum(char in vowels for char in s[:k])
        res = count

        left = 0
        for right in range(k, len(s)):
            count += (s[right] in vowels) - (s[left] in vowels)
            res = max(res, count)
            left += 1

        return res
