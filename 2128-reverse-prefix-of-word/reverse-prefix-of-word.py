class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = word.find(ch)
        res = word[:i + 1][::-1] + word[i + 1:]
        return ''.join(res)