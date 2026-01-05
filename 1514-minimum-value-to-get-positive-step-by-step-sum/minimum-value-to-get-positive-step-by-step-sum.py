class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = min_val = 0

        for i in nums:
            prefix += i
            min_val = min(min_val, prefix)
        
        # if min_val > 0:
        #     return 1
        # else:
        #     return 1 - min_val
        return 1 - min_val