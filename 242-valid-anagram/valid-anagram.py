from collections import Counter

class Solution:
    # O(n+m), O(n+m)
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)