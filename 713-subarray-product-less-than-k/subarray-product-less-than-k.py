class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0

        left = res = 0
        product = 1
        for right, num in enumerate(nums):
            product *= num
            while left <= right and product >= k:
                product /= nums[left]
                left += 1
            res += right - left + 1

        return res