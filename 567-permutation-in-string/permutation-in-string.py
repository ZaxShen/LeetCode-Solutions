from collections import Counter

class Solution:
    # O(n), O(n)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        window_size = len(s1)

        # First window
        perm1 = Counter(s1)
        perm2 = Counter(s2[:window_size])
        
        if perm1 == perm2:
            return True

        # Sliding window
        for i in range(window_size, len(s2)):
            r, l = s2[i], s2[i - window_size]
            perm2[r] += 1
            
            perm2[l] -= 1
            if perm2[l] == 0:
                perm2.pop(l)
            
            if perm1 == perm2:
                return True

        return False