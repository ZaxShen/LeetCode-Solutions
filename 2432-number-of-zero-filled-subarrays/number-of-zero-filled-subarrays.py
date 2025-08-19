from itertools import groupby

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        curr_zeros = res = 0

        for num in nums:
            if num == 0:
                curr_zeros += 1
                res += curr_zeros
            else:
                curr_zeros = 0

        return res
  