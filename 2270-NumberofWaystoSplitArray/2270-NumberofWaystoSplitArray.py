# Last updated: 8/10/2025, 10:07:35 PM
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        left_sec = res = 0
        total = sum(nums)

        for i in range(len(nums) - 1):
            left_sec += nums[i]
            right_sec = total - left_sec
            if left_sec >= right_sec:
                res += 1

        return res
        