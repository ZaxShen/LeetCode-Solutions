class Solution:
    def maxPower(self, s: str) -> int:
        left = 0
        res = 0

        while left < len(s):
            right = left
            while right < len(s) and s[left] == s[right]:
                right += 1
            res = max(res, right - left)
            left = right

        return res