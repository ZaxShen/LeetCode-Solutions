# Last updated: 8/13/2025, 2:45:33 PM
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        res = 0
        left = 0
        curr = 1

        for right, num in enumerate(nums):
            curr *= num
            while curr >= k:
                curr /= nums[left]
                left += 1
            res += right - left + 1 

        return res