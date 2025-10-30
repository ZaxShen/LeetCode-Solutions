from collections import Counter

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        count = Counter()

        for start, end in paths:
            count[start] += 1
            count[end] += 1

        
        for start, end in paths:
            if count[end] == 1:
                return end