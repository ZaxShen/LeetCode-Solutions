class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        left = prefix = 0
        
        for right, i in enumerate(nums):
            prefix += i

            while prefix >= target:
                res = min(res, right - left + 1)
                prefix -= nums[left]
                left += 1

        return res if res != float('inf') else 0
                