# Last updated: 8/14/2025, 1:15:08 PM
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(word[::-1] for word in s.split())