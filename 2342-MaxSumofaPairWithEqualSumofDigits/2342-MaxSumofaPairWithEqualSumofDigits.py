# Last updated: 8/17/2025, 6:54:01 PM
from collections import defaultdict, Counter

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        seen = defaultdict(list)

        def sum_digits(num: int) -> int:
            res = 0
            while num > 0:
                res += num % 10
                num //= 10

            return res
        
        for num in nums:
            sum_num = sum_digits(num)
            seen[sum_num].append(num)

        res = -1
        for k, v in seen.items():
            if len(v) >= 2:
                res = max(res, sum(sorted(v)[-2:]))

        return res