# Last updated: 8/13/2025, 2:54:36 PM
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sec = count = 0

        for i, num in enumerate(nums[:-1]):
            left_sec += num
            right_sec = total - left_sec
            if left_sec >= right_sec:
                count += 1

        return count