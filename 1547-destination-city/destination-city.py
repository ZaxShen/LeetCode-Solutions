class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starts = {start for start, _ in paths}

        for _, end in paths:
            if end not in starts:
                return end