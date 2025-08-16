# Last updated: 8/16/2025, 12:47:12 PM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        # expected_nums = range(n)
        max_num = n - 1
        expected_sum = max_num * n // 2
        
        return expected_sum - sum(nums)