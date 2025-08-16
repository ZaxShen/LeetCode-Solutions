# Last updated: 8/16/2025, 12:26:18 PM
class Solution:
    # O(n), O(1)
    def maxPower(self, s: str) -> int:
        left = res = 0

        while left < len(s):
            right = left
            while right < len(s) and s[left] == s[right]:
                right += 1
            res = max(res, right - left)
            left = right

        return res
