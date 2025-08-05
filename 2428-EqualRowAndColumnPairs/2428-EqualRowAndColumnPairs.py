# Last updated: 8/4/2025, 10:43:34 PM
from collections import Counter

class Solution:
    # O(n^2), O(n^2)
    def equalPairs(self, grid: list[list[int]]) -> int:
        res = 0

        # list cannot be stored in dict as an valid index
        rows = Counter([tuple(row) for row in grid])

        n_r = len(grid)
        n_c = len(grid[0])

        for r in range(n_r):
            col = [grid[c][r] for c in range(n_c)]
            col = tuple(col)
            res += rows[col]

        return res