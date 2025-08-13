# Last updated: 8/13/2025, 2:12:05 PM
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = res = sum(nums[:k])

        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k]
            res = max(res, curr)

        return res / k