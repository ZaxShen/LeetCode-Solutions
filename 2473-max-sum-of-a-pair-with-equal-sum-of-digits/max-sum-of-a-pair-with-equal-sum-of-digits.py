from collections import defaultdict

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d = defaultdict(int)
        res = -1

        for i in nums:
            k = sum(map(int, str(i)))
            if k in d:
                res = max(res, i + d[k])
                d[k] = max(d[k], i)
            else:
                d[k] = i

        return res