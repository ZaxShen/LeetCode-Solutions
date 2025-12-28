class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = win_sum = 0
        res = float('inf')

        for right, i in enumerate(nums):
            win_sum += i
            while left <= right and win_sum >= target:
                res = min(res, right - left + 1)
                win_sum -= nums[left]
                left += 1
        
        return res if res != float('inf') else 0