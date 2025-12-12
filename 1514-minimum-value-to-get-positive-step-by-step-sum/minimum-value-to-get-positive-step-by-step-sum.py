class Solution:
    # O(n), O(1)
    def minStartValue(self, nums: List[int]) -> int:
        res = prefix = 0

        for i in nums:
            prefix += i
            res = min(res, prefix)

        return -res + 1