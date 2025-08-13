# Last updated: 8/13/2025, 11:56:12 AM
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # First window
        curr = max_sum = sum(nums[:k])

        # Main window
        for i in range(k, len(nums)):
            curr += + nums[i] - nums[i - k]
            max_sum = max(max_sum, curr)

        return max_sum / k