class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix = left = 0
        res = float('inf')

        for right, num in enumerate(nums):
            prefix += num
            while prefix >= target:
                res = min(res, right - left + 1)
                prefix -= nums[left]
                left += 1

        return res if res != float('inf') else 0