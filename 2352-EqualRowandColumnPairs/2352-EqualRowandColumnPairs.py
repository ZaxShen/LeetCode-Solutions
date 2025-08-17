# Last updated: 8/17/2025, 3:38:09 PM
from collections import Counter

class Solution:
    # O(n^2), O(n^2)
    def equalPairs(self, grid: List[List[int]]) -> int:
        # Count row patterns
        rows = Counter(tuple(row) for row in grid)
        
        # Count column patterns using zip transpose
        cols = Counter(zip(*grid))
        
        # Count matching pairs
        return sum(rows[pattern] * cols[pattern] 
                  for pattern in rows 
                  if pattern in cols)