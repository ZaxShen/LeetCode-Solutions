# Last updated: 8/11/2025, 12:58:52 PM
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        
        n = len(nums)
        window_size = 2 * k + 1
        
        # Not enough elements for any valid window
        if window_size > n:
            return [-1] * n
        
        result = [-1] * n
        window_sum = sum(nums[:window_size])
        
        # Calculate averages for valid positions
        for i in range(k, n - k):
            if i == k:
                # First valid position
                result[i] = window_sum // window_size
            else:
                # Slide window: add new element, remove old element
                window_sum += nums[i + k] - nums[i - k - 1]
                result[i] = window_sum // window_size
        
        return result