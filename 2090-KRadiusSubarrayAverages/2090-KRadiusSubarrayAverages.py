# Last updated: 8/13/2025, 12:59:36 PM
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [-1] * n
        window_size = 2 * k + 1

        if n == 0:
            return nums
        if window_size > n:
            return res

        # 1st window
        window_sum = sum(nums[:window_size])
        res[k] = window_sum // window_size

        # Sliding window
        for i in range(window_size, n):
            window_sum += nums[i] - nums[i - window_size]
            res[i - k] = window_sum // window_size

        return res