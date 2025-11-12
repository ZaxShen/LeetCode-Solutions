from itertools import accumulate

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        acc = tuple(accumulate(nums))
        total = acc[-1]

        for idx, i in enumerate(nums):
            if total - acc[idx] == acc[idx] - i:
                return idx

        return -1