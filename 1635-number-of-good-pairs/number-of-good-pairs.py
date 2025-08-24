from collections import defaultdict

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = defaultdict(int)

        res = 0
        for num in nums:
            res += d[num]
            d[num] += 1

        return res