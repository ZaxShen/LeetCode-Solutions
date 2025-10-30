from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        n1 = len(s1)
        perm1 = Counter(s1)
        perm2 = Counter(s2[:n1])
        if perm1 == perm2: return True

        for i in range(n1, len(s2)):
            perm2[s2[i - n1]] -= 1
            perm2[s2[i]] += 1
            if perm1 == perm2: return True

        return False
