# Last updated: 8/13/2025, 10:01:55 AM
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        left = 0

        for right in range(len(word)):
            if word[right] == ch:
                word = list(word)
                while left < right:
                    word[left], word[right] = word[right], word[left]
                    left += 1
                    right -= 1
                word = ''.join(word)
                break

        return word