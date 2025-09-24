class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        left = win_sum = 0

        for right, num in enumerate(nums):
            win_sum += num

            while win_sum >= target:
                min_len = min(min_len, right - left + 1)
                win_sum -= nums[left]
                left += 1

        return min_len if min_len != float('inf') else 0