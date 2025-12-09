class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0
        
        product = 1
        left = res = 0

        for right, i in enumerate(nums):
            product *= i

            while left <= right and product >= k:
                product /= nums[left]
                left += 1
            
            res += right - left + 1

        return res
