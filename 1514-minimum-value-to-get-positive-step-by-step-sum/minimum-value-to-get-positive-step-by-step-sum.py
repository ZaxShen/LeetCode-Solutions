class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = min_val = 0

        for num in nums:
            prefix += num
            min_val = min(min_val, prefix)

        return -min_val + 1