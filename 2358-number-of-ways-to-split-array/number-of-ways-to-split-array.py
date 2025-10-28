from itertools import accumulate

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        acc = tuple(accumulate(nums))
        total = acc[-1]

        res = 0
        for idx, i in enumerate(nums[:-1]):
            if acc[idx] >= total - acc[idx]:
                res += 1

        return res