# Last updated: 8/18/2025, 8:51:41 AM
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = window_sum = sum(nums[:k])

        left = 0
        for right in range(k, len(nums)):
            window_sum += nums[right] - nums[left]
            res = max(res, window_sum)
            left += 1

        return res / k
