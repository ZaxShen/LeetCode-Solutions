# Last updated: 8/11/2025, 6:04:34 PM
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        try:
            index = word.index(ch) + 1
        except ValueError:
            return word

        return word[:index][::-1] + word[index:]
