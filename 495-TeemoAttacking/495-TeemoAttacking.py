# Last updated: 8/15/2025, 4:36:19 PM
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = 0

        for i in range(len(timeSeries) - 1):
            res += min(duration, timeSeries[i + 1] - timeSeries[i])

        return res + duration
