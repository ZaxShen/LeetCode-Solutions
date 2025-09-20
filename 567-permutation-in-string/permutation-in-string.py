from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        c1 = Counter(s1)
        c2 = Counter(s2[:len(s1)])  # First window
        if c1 == c2:
            return True

        left = 0
        for right in range(len(s1), len(s2)):
            c2[s2[right]] += 1
            c2[s2[left]] -= 1
            left += 1

            if c1 == c2:
                return True

        return False


