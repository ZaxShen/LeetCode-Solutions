from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cols = (tuple(col) for col in zip(*grid))
        cols = Counter(cols)

        res = 0
        for pattern in grid:
            pattern = tuple(pattern)
            if pattern in cols:
                res += cols[pattern]

        return res