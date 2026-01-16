class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d = {}
        res = -1

        for i in nums:
            digits = sum(map(int, str(i)))
            if digits in d:
                res = max(res, i + d[digits])
                d[digits] = max(d[digits], i)
            else:
                d[digits] = i

        return res