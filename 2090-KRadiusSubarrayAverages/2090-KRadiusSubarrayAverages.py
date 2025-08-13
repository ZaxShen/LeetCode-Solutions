# Last updated: 8/13/2025, 2:40:12 PM
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums

        n = len(nums)
        window_size = 2 * k + 1
        res = [-1] * n

        if window_size > n:
            return res

        # First window
        window_sum = sum(nums[:window_size])
        res[k] = window_sum // window_size

        # Sliding window
        for i in range(window_size, n):
            window_sum += nums[i] - nums[i - window_size]
            res[i - k] = window_sum // window_size

        return res