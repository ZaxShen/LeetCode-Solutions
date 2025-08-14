# Last updated: 8/14/2025, 3:39:48 PM
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sec = res = 0

        for i, v in enumerate(nums[:-1]):
            left_sec += v
            right_sec = total - left_sec
            if left_sec >= right_sec:
                res += 1

        return res

            