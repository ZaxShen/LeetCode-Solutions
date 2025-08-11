# Last updated: 8/11/2025, 5:42:02 PM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) != 1:
            left = 0

            for right in range(len(nums)):
                if nums[right] != 0:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
