class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        # Frist window
        res = win_cnt = sum(map(lambda char: char in vowels, s[:k]))

        # Slide window
        for i in range(k, len(s)):
            win_cnt += (s[i] in vowels) - (s[i - k] in vowels)
            res = max(res, win_cnt)

            if res == k:
                break

        return res