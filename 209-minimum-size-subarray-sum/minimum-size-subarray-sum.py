class Solution:
    # O(n), O(n)
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        win_sum = 0
        left = 0
        res = float('inf')

        for right, i in enumerate(nums):
            win_sum += i
            while win_sum >= target:
                res = min(res, right - left + 1)
                win_sum -= nums[left]
                left += 1

        return res if res != float('inf') else 0
