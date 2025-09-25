from itertools import accumulate

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        acc = tuple(accumulate(nums))

        for i in range(len(nums)):
            left_sec = acc[i] - nums[i]
            right_sec = total - acc[i]
            if left_sec == right_sec:
                return i

        return -1