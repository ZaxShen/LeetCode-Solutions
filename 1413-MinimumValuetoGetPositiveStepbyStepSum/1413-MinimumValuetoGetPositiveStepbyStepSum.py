# Last updated: 8/11/2025, 12:23:35 PM
class Solution:
    # O(n), O(1)
    def minStartValue(self, nums: List[int]) -> int:
        curr = min_start_val = 0

        for num in nums:
            curr += num
            min_start_val = min(min_start_val, curr)

        return -min_start_val + 1