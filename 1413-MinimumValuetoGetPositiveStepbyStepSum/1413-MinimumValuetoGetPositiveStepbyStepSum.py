# Last updated: 8/13/2025, 1:01:04 AM
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        curr = 0
        res = float("inf")

        for num in nums:
            curr += num
            res = min(res, curr)

        return max(-res + 1, 1)
