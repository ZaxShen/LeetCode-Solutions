# Last updated: 8/11/2025, 11:09:10 AM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        pos = right
        res = [0] * len(nums)

        # Handle edge cases for better performance
        if nums[left] >= 0:
            return [num ** 2 for num in nums]
        if nums[right] <= 0:
            return [num ** 2 for num in nums][::-1]

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
