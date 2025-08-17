# Last updated: 8/17/2025, 5:29:44 PM
class Solution:
    # O(n), O(1)
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1

        # Edge Cases Handling
        if nums[left] >= 0:
            return [num ** 2 for num in nums]
        elif nums[right] <= 0:
            return [num ** 2 for num in nums[::-1]]

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
