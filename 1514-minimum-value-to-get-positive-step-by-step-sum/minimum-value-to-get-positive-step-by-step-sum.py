class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        curr = min_start_val = 0

        for i in nums:
            curr += i
            min_start_val = min(curr, min_start_val)

        return -min_start_val + 1