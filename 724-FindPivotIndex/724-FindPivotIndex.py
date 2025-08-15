# Last updated: 8/15/2025, 4:32:39 PM
class Solution:
    # O(n), O(1)
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sec = res = 0

        for i, num in enumerate(nums):
            right_sec = total - left_sec - num
            if left_sec == right_sec:
                return i
            left_sec += num

        return -1
