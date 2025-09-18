from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cols = Counter(tuple(col) for col in zip(*grid))

        res = 0
        for pattern in grid:
            res += cols[tuple(pattern)]

        return res