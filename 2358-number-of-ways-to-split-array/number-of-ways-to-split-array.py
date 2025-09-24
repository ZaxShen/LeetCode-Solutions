from itertools import accumulate

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        total = sum(nums)
        acc = tuple(accumulate(nums))

        res = 0
        for i in range(len(nums) - 1):
            left_sec = acc[i]
            right_sec = total - left_sec
            if left_sec >= right_sec:
                res += 1

        return res