# Last updated: 8/11/2025, 12:06:42 PM
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        left_sec = count = 0
        total = sum(nums)

        for i in range(len(nums) - 1):
            left_sec += nums[i]
            right_sec = total - left_sec
            if left_sec >= right_sec:
                count += 1

        return count
