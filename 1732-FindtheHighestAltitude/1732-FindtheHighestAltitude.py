# Last updated: 8/11/2025, 7:56:05 PM
from itertools import accumulate

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = max(accumulate(gain))
        return res if res > 0 else 0