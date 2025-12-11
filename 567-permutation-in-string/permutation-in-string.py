from collections import Counter

class Solution:
    # O(n), O(k)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge Case
        if len(s1) > len(s2): return False

        c1 = Counter(s1)
        c2 = Counter(s2[:len(s1)])
        if c1 == c2: return True

        left = 0

        for i in s2[len(s1):]:
            c2[i] += 1
            c2[s2[left]] -= 1
            left += 1
            
            if c1 == c2: return True

        return False
