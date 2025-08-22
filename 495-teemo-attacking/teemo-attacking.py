class Solution:
    # O(n), O(1)
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = 0

        for i in range(len(timeSeries) - 1):
            res += min(duration, timeSeries[i + 1] - timeSeries[i])
        res += duration  # For final second

        return res