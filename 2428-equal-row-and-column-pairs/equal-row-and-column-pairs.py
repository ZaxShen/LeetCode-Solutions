from collections import Counter

class Solution:
    # O(n^2), O(n^2)
    def equalPairs(self, grid: List[List[int]]) -> int:
        cols = Counter(tuple(col) for col in zip(*grid))

        res = 0
        for pattern in grid:
            pattern = tuple(pattern)
            res += cols[pattern]

        return res