# Last updated: 8/13/2025, 1:18:10 PM
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        curr = 1
        left = 0
        res = 0

        if k <= 1:
            return 0

        for right, num in enumerate(nums):
            curr *= num
            while curr >= k:
                curr /= nums[left]
                left += 1
            res += right - left + 1

        return res

