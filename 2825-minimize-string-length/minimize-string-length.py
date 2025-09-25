from collections import Counter

class Solution:
    # O(n), O(n)
    def minimizedStringLength(self, s: str) -> int:
        count = Counter(s)
        
        return len(count)