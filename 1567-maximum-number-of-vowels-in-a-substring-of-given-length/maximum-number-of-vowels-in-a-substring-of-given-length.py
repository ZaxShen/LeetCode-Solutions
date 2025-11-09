class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        res = 0

        res = count = sum(i in vowels for i in s[:k])

        left = 0
        for right in range(k, len(s)):
            count += (s[right] in vowels) - (s[left] in vowels)
            res = max(res, count)
            left += 1
            if res == k:
                return res

        return res