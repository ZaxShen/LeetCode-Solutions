# Last updated: 8/4/2025, 10:43:43 PM
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # Situation 1: k = 0
        if k == 0:
            return nums

        n = len(nums)
        avgs = [-1] * n
        window_size = 2 * k + 1
        # Situation 2: window_size > n
        if window_size > n:
            return avgs

        # Situation 3: starting from k, we calculate the average
        window_sum = sum(nums[:window_size])
        avgs[k] = window_sum // window_size
        for i in range(window_size, n):
            window_sum += nums[i] - nums[i - window_size]
            avgs[i - k] = window_sum // window_size

        return avgs