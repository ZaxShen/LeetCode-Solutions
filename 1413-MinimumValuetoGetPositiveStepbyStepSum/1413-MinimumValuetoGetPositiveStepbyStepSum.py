# Last updated: 8/13/2025, 1:49:08 AM
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        curr = res = 0

        for num in nums:
            curr += num
            res = min(res, curr)

        return -res + 1