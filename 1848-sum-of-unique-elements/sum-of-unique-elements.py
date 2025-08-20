from collections import Counter

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counter = Counter(nums)

        res = 0
        for k, v in counter.items():
            if v == 1:
                res += k

        return res
