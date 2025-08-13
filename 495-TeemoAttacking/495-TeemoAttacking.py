# Last updated: 8/13/2025, 1:15:24 AM
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = 0
        
        for i in range(len(timeSeries) - 1):
            res += min(duration, timeSeries[i + 1] - timeSeries[i])

        return res + duration