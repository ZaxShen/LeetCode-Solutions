# Last updated: 8/11/2025, 6:22:59 PM
class Solution:
    # O(n), O(1)
    def reversePrefix(self, word: str, ch: str) -> str:
        word = list(word)
        left = 0

        for right in range(len(word)):
            if word[right] == ch:
                while left < right:
                    word[left], word[right] = word[right], word[left]
                    left += 1
                    right -= 1
                return ''.join(word)

        return ''.join(word)