# Last updated: 8/14/2025, 1:46:05 AM
from collections import Counter

class Solution:
    def countElements(self, arr: List[int]) -> int:
        hash_set = set(arr)
        count = 0

        for i in arr:
            if i + 1 in hash_set:
                count += 1
        
        return count
        