# Last updated: 8/13/2025, 10:11:02 AM
class Solution:
    # O(n), O(1)
    def largestAltitude(self, gain: List[int]) -> int:
        curr = max_alt = 0

        for g in gain:
            curr += g
            max_alt = max(max_alt, curr)

        return max_alt if max_alt > 0 else 0