# Last updated: 8/11/2025, 11:07:46 AM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        pos = right
        res = [0] * len(nums)

        while left <= right:
            left_sq, right_sq = nums[left] ** 2, nums[right] ** 2
            if left_sq < right_sq:
                res[pos] = right_sq
                right -= 1
            else:
                res[pos] = left_sq
                left += 1
            pos -= 1

        return res
