# Last updated: 8/4/2025, 10:45:12 PM
from collections import Counter

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if Counter(target) != Counter(arr):
            return False

        return True