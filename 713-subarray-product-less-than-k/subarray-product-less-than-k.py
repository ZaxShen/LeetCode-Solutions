class Solution:
    # O(n), O(1)
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        product = 1
        left = count = 0
        for right, num in enumerate(nums):
            product *= num

            while product >= k:
                product /= nums[left]
                left += 1
            count += right - left + 1

        return count