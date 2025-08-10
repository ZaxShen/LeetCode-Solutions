# Last updated: 8/9/2025, 11:56:35 PM
class Solution:
    # O(n), O(1)
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        left = res = 0
        curr = 1
        for right, v in enumerate(nums):
            curr *= v
            while curr >= k:
                curr /= nums[left]
                left += 1
            res += right - left + 1

        return res
