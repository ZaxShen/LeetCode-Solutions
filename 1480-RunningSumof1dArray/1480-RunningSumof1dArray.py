# Last updated: 8/13/2025, 11:28:59 AM
from itertools import accumulate

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return list(accumulate(nums))