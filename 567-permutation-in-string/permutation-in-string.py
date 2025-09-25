from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        n = len(s1)
        perm_s1 = Counter(s1)
        perm_s2 = Counter(s2[:n])
        if perm_s2 >= perm_s1:
            return True

        for i in range(n, len(s2)):
            perm_s2[s2[i]] += 1
            perm_s2[s2[i - n]] -= 1
            if perm_s2 >= perm_s1:
                return True

        return False
