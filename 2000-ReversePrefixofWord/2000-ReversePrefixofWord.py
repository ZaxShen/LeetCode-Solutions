# Last updated: 8/13/2025, 9:48:06 AM
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        try:
            index = word.index(ch)
        except ValueError:
            return word

        return word[:index + 1][::-1] + word[index + 1:]