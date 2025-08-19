class Solution:
    # O(n), O(n)
    def destCity(self, paths: List[List[str]]) -> str:
        starts = {start for start, _ in paths}
        
        # Early termination
        for _, end in paths:
            if end not in starts:
                return end