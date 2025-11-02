class Solution:
    # O(n), O(1)
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # Edge Case
        if k <= 1: return 0

        left = res = 0
        win_prod = 1

        for right, i in enumerate(nums):
            win_prod *= i
            while left <= right and win_prod >= k:
                win_prod /= nums[left]
                left += 1
            res += right - left + 1

        return res