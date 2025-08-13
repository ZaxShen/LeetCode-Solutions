# Last updated: 8/13/2025, 12:54:15 AM
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sec = 0

        for i, num in enumerate(nums):
            right_sec = total - left_sec - num
            if left_sec == right_sec:
                return i
            left_sec += num

        return -1