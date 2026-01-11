class Solution:
    # O(n), O(k)
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')

        # First window
        res = win_cnt = sum(i in vowels for i in s[:k])

        # Sldiing window
        for i in range(k, len(s)):
            win_cnt += (s[i] in vowels) - (s[i - k] in vowels)
            res = max(res, win_cnt)
            
            if res == k:
                return res

        return res