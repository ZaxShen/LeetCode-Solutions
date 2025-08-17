# Last updated: 8/17/2025, 10:32:02 AM
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = res = 0
        for right, num in enumerate(nums):
            if num == 0:
                k -= 1
            
            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            res = max(res, right - left + 1)

        return res