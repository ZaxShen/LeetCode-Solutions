class Solution:
    # O(n), O(k)
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k >= len(nums): return sum(nums) / len(nums)

        # First window
        win_sum = res = sum(nums[:k])

        # Sliding window
        for i in range(k, len(nums)):
            win_sum += nums[i] - nums[i - k]
            res = max(res, win_sum)

        return res / k