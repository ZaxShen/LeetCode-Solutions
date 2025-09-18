class Solution:
    # O(n)
    def destCity(self, paths: List[List[str]]) -> str:
        starts = {start for start, _ in paths}

        for _, destination in paths:
            if destination not in starts:
                return destination
