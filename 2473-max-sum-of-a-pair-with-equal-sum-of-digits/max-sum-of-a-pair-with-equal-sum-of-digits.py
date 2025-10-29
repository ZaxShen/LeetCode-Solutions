from collections import defaultdict

class Solution:
    # O(n), O(k)
    def maximumSum(self, nums: List[int]) -> int:
        d = defaultdict(int)
        res = -1

        for i in nums:
            k = sum(map(int, str(i)))

            if k in d:
                res = max(res, d[k] + i)
            
            d[k] = max(d[k], i)

        return res


