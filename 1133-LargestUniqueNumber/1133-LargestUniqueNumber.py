# Last updated: 8/16/2025, 11:26:54 PM
from collections import Counter

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)

        max_num = -1
        for k, v in counter.items():
            if v == 1:
                max_num = max(max_num, k)

        return max_num
