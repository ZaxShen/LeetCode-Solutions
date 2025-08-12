# Last updated: 8/12/2025, 7:19:42 PM
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = 0
        for i in range(len(timeSeries) - 1):
            if timeSeries[i] + duration < timeSeries[i + 1]:
                res += duration
            else:
                res += timeSeries[i + 1] - timeSeries[i]

        return res + duration
