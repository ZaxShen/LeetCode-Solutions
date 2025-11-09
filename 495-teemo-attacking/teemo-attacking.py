class Solution:
    # O(n), O(1)
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = 0

        for i in range(len(timeSeries) - 1):
            timeSpan = timeSeries[i + 1] - timeSeries[i]
            res += min(timeSpan, duration)
        res += duration

        return res