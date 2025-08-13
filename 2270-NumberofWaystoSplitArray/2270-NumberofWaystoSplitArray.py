# Last updated: 8/13/2025, 1:53:20 PM
class Solution:
    # O(n), O(1)
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sec = res = 0

        # Avoid the rightest item
        for num in nums[:-1]:
            left_sec += num
            right_sec = total - left_sec
            if left_sec >= right_sec:
                res += 1

        return res
