class Solution:
    # O(n), O(1)
    def minStartValue(self, nums: List[int]) -> int:
        prefix = min_val = 0

        for i in nums:
            prefix += i
            min_val = min(min_val, prefix)

        return -min_val + 1