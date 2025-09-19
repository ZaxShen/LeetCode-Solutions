from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)
        res = -1

        for i, v in count.items():
            if i == v:
                res = max(res, i)

        return res