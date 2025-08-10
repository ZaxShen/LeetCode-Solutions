# Last updated: 8/10/2025, 3:10:58 PM
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        product = 1
        left = count = 0
        for right, v in enumerate(nums):
            product *= v
            while product >= k:
                product /= nums[left]
                left += 1
            count += right - left + 1

        return count