# Last updated: 8/11/2025, 8:57:30 PM
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0

        for right, num in enumerate(nums):
            if num == 0:
                k -= 1
            
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1

        return right - left + 1