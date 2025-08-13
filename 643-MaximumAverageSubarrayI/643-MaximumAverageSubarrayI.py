# Last updated: 8/13/2025, 7:35:12 PM
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # if k <= 1:
        #     return nums[0]

        # First window
        res = curr = sum(nums[:k])

        # Sliding window
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k]
            res = max(res, curr)

        return res / k