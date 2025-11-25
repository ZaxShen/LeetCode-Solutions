class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix = res = 0

        for i in gain:
            prefix += i
            res = max(res, prefix)

        return res
