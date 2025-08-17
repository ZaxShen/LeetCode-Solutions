# Last updated: 8/17/2025, 3:41:39 PM
from collections import Counter

class Solution:
    # O(n^3), O(n^2)
    def equalPairs(self, grid: list[list[int]]) -> int:
        res = 0

        # list cannot be stored in dict as an valid index
        rows = Counter(tuple(row) for row in grid)

        n_rows = len(grid)
        n_cols = len(grid[0])
        for r in range(n_rows):
            col = tuple(grid[c][r] for c in range(n_cols))
            res += rows[col]

        return res