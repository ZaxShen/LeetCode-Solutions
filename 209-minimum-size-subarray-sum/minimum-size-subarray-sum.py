class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        left = curr = 0

        for right, num in enumerate(nums):
            curr += num
            while curr >= target:
                min_len = min(min_len, right - left + 1)
                curr -= nums[left]
                left += 1

        return min_len if min_len != float('inf') else 0