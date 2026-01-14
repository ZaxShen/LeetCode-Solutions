class Solution:
    # O(n), O(1)
    def maximumSum(self, nums: List[int]) -> int:
        d = dict()
        res = -float('inf')

        for i in nums:
            digits = sum(map(int, str(i)))
            if digits in d:
                res = max(res, d[digits] + i)
                d[digits] = max(d[digits], i)
            else:
                d[digits] = i

        return res if res != -float('inf') else -1