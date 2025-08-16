# Last updated: 8/16/2025, 12:17:37 PM
class Solution:
    # O(n), O(1)
    def maxPower(self, s: str) -> int:
        count = res = 1

        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                count += 1
                res = max(res, count)
            else:
                count = 1
        return res
