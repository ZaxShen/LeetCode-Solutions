# Last updated: 8/10/2025, 12:25:17 AM
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = curr = 0
        res = float('inf')

        for right, v in enumerate(nums):
            curr += v
            while curr >= target:
                res = min(res, right - left + 1)
                curr -= nums[left]
                left += 1
            
        if res == float('inf'):
            return 0
        return res


        