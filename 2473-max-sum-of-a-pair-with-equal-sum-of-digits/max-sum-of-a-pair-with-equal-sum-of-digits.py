from collections import defaultdict

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def helper(num: int) -> int:
            res = 0
            
            while num != 0:
                res += num % 10
                num = num // 10
            res + num

            return res

        seen = defaultdict(int)
        res = -1

        for i in nums:
            digits = helper(i)
            if digits in seen:
                res = max(res, seen[digits] + i)
            #     if seen[digits] < i:
            #         seen[digits] = i
            # else:
            seen[digits] = max(seen[digits], i)

        return res