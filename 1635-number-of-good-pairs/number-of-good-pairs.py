class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = {}
        res = 0

        for i in nums:
            res += d.get(i, 0)
            d[i] = d.get(i, 0) + 1

        return res