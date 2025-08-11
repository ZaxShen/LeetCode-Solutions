# Last updated: 8/10/2025, 9:26:05 PM
from itertools import accumulate

class Solution:
    # O(n), O(1)
    def runningSum(self, nums: List[int]) -> List[int]:
        return list(accumulate(nums))