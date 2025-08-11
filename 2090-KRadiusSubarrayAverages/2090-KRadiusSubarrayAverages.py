# Last updated: 8/11/2025, 12:56:18 PM
class Solution:
    # O(n), O(n)
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums

        n = len(nums)
        avgs = [-1] * n
        window_size = 2 * k + 1

        if window_size > n:
            return avgs

        window_sum = sum(nums[:window_size])
        avgs[k] = window_sum // window_size
        for i in range(window_size, n):
            window_sum += nums[i] - nums[i - window_size]
            avgs[i - k] = window_sum // window_size

        return avgs

