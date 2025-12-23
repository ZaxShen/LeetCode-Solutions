class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        res = win_count = sum(map(lambda i: i in vowels, s[:k]))

        if res == k: return res

        for i in range(k, len(s)):
            win_count += (s[i] in vowels) - (s[i - k] in vowels)
            res = max(res, win_count)
            # Early Termination
            if res == k: return res

        return res