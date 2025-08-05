# Last updated: 8/4/2025, 10:46:25 PM
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = right = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
        
        return right - left + 1