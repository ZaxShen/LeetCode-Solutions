# Last updated: 8/11/2025, 1:00:10 PM
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        
        n = len(nums)
        window_size = 2 * k + 1
        avgs = [-1] * n
        
        # Not enough elements for any valid window
        if window_size > n:
            return avgs
        
        window_sum = sum(nums[:window_size])
        
        # Calculate averages for valid positions
        for i in range(k, n - k):
            if i == k:
                # First valid position
                avgs[i] = window_sum // window_size
            else:
                # Slide window: add new element, remove old element
                window_sum += nums[i + k] - nums[i - k - 1]
                avgs[i] = window_sum // window_size
        
        return avgs