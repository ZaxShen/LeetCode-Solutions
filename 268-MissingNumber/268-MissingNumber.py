# Last updated: 8/15/2025, 5:36:31 PM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected_sum = sum(range(len(nums) + 1))
        return expected_sum - sum(nums)