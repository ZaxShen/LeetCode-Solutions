class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix = res = 0

        for g in gain:
            prefix += g
            res = max(res, prefix)

        return res