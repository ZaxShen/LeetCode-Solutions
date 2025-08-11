# Last updated: 8/11/2025, 5:44:33 PM
class Solution:
	# O(n), O(1)
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0 and nums[left] == 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            if nums[left] != 0:
                left += 1