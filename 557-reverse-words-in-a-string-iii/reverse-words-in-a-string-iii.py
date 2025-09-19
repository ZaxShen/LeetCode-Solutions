class Solution:
    # O(n), O(1)
    def reverseWords(self, s: str) -> str:
        s = s.split()
        res = [word[::-1] for word in s]

        return " ".join(res)