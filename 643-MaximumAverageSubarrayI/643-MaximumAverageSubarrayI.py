# Last updated: 8/10/2025, 12:08:20 AM
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = curr = sum(nums[:k])
        left = 0

        for right in range(k, len(nums)):
            curr += nums[right] - nums[left]
            res = max(res, curr)
            left += 1

        return res / k
