from collections import Counter

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = Counter(nums)

        res = -1
        for k, v in count.items():
            if v == 1:
                res = max(res, k)

        return res