# Last updated: 8/12/2025, 6:38:24 PM
class Solution:
    # O(n), O(1)
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sec = res = 0

        for right, num in enumerate(nums[:-1]):
            left_sec += num
            right_sec = total - left_sec
            if left_sec >= right_sec:
                res += 1

        return res

