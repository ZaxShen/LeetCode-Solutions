# Last updated: 8/16/2025, 12:55:17 PM
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        product = 1
        left = res = 0

        if k <= 1:
            return 0

        for right, num in enumerate(nums):
            product *= num

            while product >= k:
                product /= nums[left]
                left += 1
            
            res += right - left + 1

        return res