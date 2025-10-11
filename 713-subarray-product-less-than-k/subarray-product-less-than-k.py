class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0

        res = 0
        prefix = 1
        left = 0

        for right, v in enumerate(nums):
            prefix *= v

            while left <= right and prefix >= k:
                prefix /= nums[left]
                left += 1
            res += right - left + 1

        return res