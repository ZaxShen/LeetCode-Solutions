from collections import defaultdict

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        A, B = zip(*paths)
        res = set(B) - set(A)
        
        return list(res)[0]
