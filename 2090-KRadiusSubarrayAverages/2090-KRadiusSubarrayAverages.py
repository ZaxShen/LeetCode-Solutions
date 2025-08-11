# Last updated: 8/11/2025, 12:36:04 PM
from itertools import accumulate

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        prefix_sum = list(accumulate(nums))
        res = []
        n = 2 * k + 1

        for i in range(len(nums)):
            left = i - k
            right = i + k
            if 0 <= left and right < len(nums):
                _ = prefix_sum[right] - prefix_sum[left] + nums[left]
                res.append(_ // n)
            else:
                res.append(-1)

        return res
