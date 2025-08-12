# Last updated: 8/11/2025, 8:01:42 PM
from itertools import accumulate

class Solution:
    # O(n), O(1)
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt = curr_alt = 0

        for point in gain:
            curr_alt += point
            max_alt = max(max_alt, curr_alt)

        return max_alt