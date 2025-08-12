# Last updated: 8/12/2025, 6:36:37 PM
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)
        left = curr = res = 0

        for right, num in enumerate(nums[:-1]):
            curr += num
            if curr >= total - curr:
                res += 1

        return res

