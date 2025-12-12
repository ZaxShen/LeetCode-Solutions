class Solution:
    # O(n), O(1)
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # Edge Cases
        if k == 0:
            return nums
        elif 2 * k + 1 > len(nums):
            return [-1] * len(nums)

        # First window
        win_size = 2 * k + 1
        win_sum = sum(nums[:win_size])
        win_avg = win_sum // win_size
        res = [-1] * len(nums)
        res[k] = win_avg
        
        # Sliding Window
        for i in range(win_size, len(nums)):
            win_sum += nums[i] - nums[i - win_size]
            win_avg = win_sum // win_size
            res[i - k] = win_avg

        return res