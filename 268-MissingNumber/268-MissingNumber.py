# Last updated: 8/16/2025, 12:45:46 PM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        expected_nums = range(n)
        return sum(expected_nums) - sum(nums)