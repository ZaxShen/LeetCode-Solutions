# Last updated: 8/10/2025, 12:05:29 AM
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left, right = 0, k
        res = curr = sum(nums[:k])
        while right < len(nums):
            curr = curr + nums[right] - nums[left]
            res = max(res, curr)
            left += 1
            right += 1

        return res / k
