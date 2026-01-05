class Solution:
    # O(n), O(1)
    def minStartValue(self, nums: List[int]) -> int:
        prefix = 0
        min_val = float('inf')

        for i in nums:
            prefix += i
            min_val = min(min_val, prefix)

        return 1 if min_val > 0 else 1 - min_val
