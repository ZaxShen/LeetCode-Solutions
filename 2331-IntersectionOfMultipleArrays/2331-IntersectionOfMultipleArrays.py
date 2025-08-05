# Last updated: 8/4/2025, 10:43:39 PM
from collections import defaultdict

class Solution:
    # O(nlogn), O(n*m)
    def intersection(self, nums: list[list[int]]) -> list[int]:
        res = defaultdict(int)

        for arr in nums:
            for i in arr:
                res[i] += 1

        res = [k for k, v in res.items() if v == len(nums)]
        res = sorted(res)

        return res