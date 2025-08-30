class Solution:
    # O(n), O(1)
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')

        # First window
        # res = window_count = sum(char in vowels for char in s[:k])
        res = window_count = sum(map(lambda char: char in vowels, s[:k]))

        # Slide window
        for i in range(k, len(s)):
            window_count += (s[i] in vowels) - (s[i - k] in vowels)
            res = max(res, window_count)

            if res == k:
                return res

        return res
            