from collections import Counter

class Solution:
    # O(n), O(k)
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # n * (n - 1) / 2
        count = Counter(nums)

        res = 0
        for v in count.values():
            res += v * (v - 1) / 2

        return int(res)
