class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        res = count = sum(map(lambda x: x in vowels, s[:k]))

        for i in range(k, len(s)):
            count += (s[i] in vowels) - (s[i - k] in vowels)
            res = max(res, count)
            if res == k:
                return res

        return res

