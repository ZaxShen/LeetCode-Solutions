# Last updated: 8/4/2025, 10:44:09 PM
from collections import Counter

class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        res = 0
        count = Counter(nums)

        for num, n in count.items():
            if n == 1:
                res += num

        return res