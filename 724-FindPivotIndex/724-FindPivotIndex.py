# Last updated: 8/11/2025, 8:24:12 PM
from itertools import accumulate

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = list(accumulate(nums))
        total = prefix_sum[-1]

        if total == prefix_sum[0]:
            return 0

        for i, num in enumerate(prefix_sum):
            if i > 0 and total - num == prefix_sum[i - 1]:
                return i

        return -1