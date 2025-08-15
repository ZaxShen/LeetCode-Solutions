# Last updated: 8/15/2025, 5:53:27 PM
class Solution:
    # O(n), O(1)
    def missingNumber(self, nums: List[int]) -> int:
        # Expected nums: range(len(nums) + 1)
        n = len(nums) + 1
        # So max num of nums should be
        max_num = n - 1
        # According to Gauss' Formula
        expected_sum = max_num * n // 2
        actual_sum = sum(nums)

        return expected_sum - actual_sum