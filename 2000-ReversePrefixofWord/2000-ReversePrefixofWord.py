# Last updated: 8/11/2025, 6:22:37 PM
class Solution:
    # O(n), O(1)
    def reversePrefix(self, word: str, ch: str) -> str:
        word = list(word)
        left = right = 0

        while right < len(word):
            if word[right] == ch:
                while left < right:
                    word[left], word[right] = word[right], word[left]
                    left += 1
                    right -= 1
                return ''.join(word)
            right += 1

        return ''.join(word)