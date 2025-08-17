# Last updated: 8/17/2025, 3:27:07 PM
from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = Counter()
        cols = Counter()

        for row in grid:
            rows[tuple(row)] += 1
        
        for col in zip(*grid):
            cols[col] += 1

        print(rows)
        print(cols)
        res = 0
        for row in rows:
            if row in cols:
                res += rows[row] * cols[row]

        return res