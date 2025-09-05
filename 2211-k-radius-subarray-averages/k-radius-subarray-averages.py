class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        if len(nums) < 2 * k + 1:
            return [-1] * len(nums)

        # First window
        win_size = 2 * k + 1
        win_sum = sum(nums[:win_size])
        win_avg = win_sum // win_size
        res = [-1] * len(nums)
        res[k] = win_avg

        # Slide window
        for i in range(win_size, len(nums)):
            win_sum += nums[i] - nums[i - win_size]
            win_avg = win_sum // win_size
            res[i - k] = win_avg

        return res