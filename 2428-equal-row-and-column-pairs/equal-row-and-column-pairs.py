from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cols = zip(*grid)
        col_count = Counter(cols)

        res = 0
        for row in grid:
            row = tuple(row)
            if row in col_count:
                res += col_count[row]

        return res
