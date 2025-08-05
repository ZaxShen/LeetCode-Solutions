# Last updated: 8/4/2025, 10:45:16 PM
from collections import defaultdict

class Solution:
    # O(n), O(n)
    def destCity(self, paths: list[list[str]]) -> str:
        start, end = set(), set()

        for path in paths:
            start.add(path[0])
            end.add(path[1])

        return list(end - start)[0]

