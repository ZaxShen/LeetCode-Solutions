class Solution:
    # O(n), O(k)
    def maximumSum(self, nums: List[int]) -> int:
        mapping = dict()
        res = -1

        def helper(num: int) -> str:
            res = 0
            while num != 0:
                res += num % 10
                num = num // 10

            return res + num

        for i in nums:
            digits = helper(i)
            if digits in mapping:
                res = max(res, mapping[digits] + i)
                mapping[digits] = max(mapping[digits], i)
            else:
                mapping[digits] = i

        return res