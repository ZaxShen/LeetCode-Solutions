# Last updated: 8/4/2025, 10:43:37 PM
class Solution:
    # O(n), O(1)
    def waysToSplitArray(self, nums: list[int]) -> int:
        ans = left_sec = 0
        total = sum(nums)

        for i in range(len(nums) - 1):
            left_sec += nums[i]
            right_sec = total - left_sec
            if left_sec >= right_sec:
                ans += 1

        return ans