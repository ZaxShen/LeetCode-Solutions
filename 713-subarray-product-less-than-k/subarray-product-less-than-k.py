class Solution:
    # O(n), O(1)
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        win_prod = 1
        left = res = 0

        for right, i in enumerate(nums):
            win_prod *= i
            while left <= right and win_prod >= k:
                win_prod /= nums[left]
                left += 1
            res += right - left + 1

        return res
