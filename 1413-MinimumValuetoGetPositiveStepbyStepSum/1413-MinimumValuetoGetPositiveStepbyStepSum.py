# Last updated: 8/15/2025, 5:32:44 PM
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        curr = res = 0

        for num in nums:
            curr += num
            res = min(res, curr)

        return -res + 1