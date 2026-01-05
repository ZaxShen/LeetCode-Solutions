class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = 0
        min_val = float('inf')

        for i in nums:
            prefix += i
            min_val = min(min_val, prefix)
        
        if min_val > 0:
            return 1
        else:
            return 1 - min_val