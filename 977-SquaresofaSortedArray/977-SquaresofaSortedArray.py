# Last updated: 8/17/2025, 5:23:22 PM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        res = [0] * len(nums)
        pos = right

        while left <= right:
            sq_left, sq_right = nums[left] ** 2, nums[right] ** 2
            if sq_left < sq_right:
                res[pos] = sq_right
                right -= 1
            else:
                res[pos] = sq_left
                left += 1
            pos -= 1
        
        return res
