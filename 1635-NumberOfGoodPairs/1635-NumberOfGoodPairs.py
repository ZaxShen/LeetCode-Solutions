# Last updated: 8/5/2025, 12:18:58 AM
from collections import defaultdict

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count = defaultdict(int)
        res = 0

        for num in nums:
            res += count[num]
            count[num] += 1
        
        return res