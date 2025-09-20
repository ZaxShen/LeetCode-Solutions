class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        win_sum = sum(nums[:k])
        res = win_sum

        for i in range(k, len(nums)):
            win_sum += nums[i] - nums[i - k]
            res = max(res, win_sum)

        return res / k