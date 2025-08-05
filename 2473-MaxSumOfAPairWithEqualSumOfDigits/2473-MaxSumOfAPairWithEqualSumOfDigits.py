# Last updated: 8/4/2025, 10:43:31 PM
from collections import defaultdict

class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        d = defaultdict(int)
        max_sum = -1

        for i in nums:
            sum_digits = sum(map(int, str(i)))
            if sum_digits in d:
                max_sum = max(max_sum, d[sum_digits] + i)
            # only stores the greatest num
            d[sum_digits] = max(i, d[sum_digits])

        return max_sum