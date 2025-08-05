# Last updated: 8/4/2025, 10:45:25 PM
from collections import Counter

class Solution:
    def findLucky(self, arr: list[int]) -> int:
        count = Counter(arr)

        res = -1
        for k, v in count.items():
            if k == v:
                res = max(res, k)

        return res
        