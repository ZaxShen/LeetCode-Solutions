from collections import Counter

class Solution:
    # O(n), O(k)
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)

        res = -1
        for k, v in count.items():
            if k == v:
                res = max(res, k)

        return res