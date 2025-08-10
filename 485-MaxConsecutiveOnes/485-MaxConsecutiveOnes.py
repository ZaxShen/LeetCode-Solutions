# Last updated: 8/10/2025, 12:47:14 AM
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        left = res = 0

        while left < len(nums):
            right = left
            while right < len(nums) and nums[right] == nums[left]:
                right += 1
            if nums[left] == 1:
                res = max(res, right - left)
            left = right
            
        return res
