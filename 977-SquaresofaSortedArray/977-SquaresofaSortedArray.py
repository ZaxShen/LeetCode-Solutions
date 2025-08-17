# Last updated: 8/17/2025, 5:47:47 PM
class Solution:
    # O(n), O(1)
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1

        # Edge Cases Handling
        if nums[left] >= 0:
            return [num ** 2 for num in nums]
        elif nums[right] <= 0:
            return [num ** 2 for num in reversed(nums)]

        res = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            abs_left, abs_right = abs(nums[left]), abs(nums[right])
            if abs_left < abs_right:
                res[i] = abs_right ** 2
                right -= 1
            else:
                res[i] = abs_left ** 2
                left += 1
        
        return res
