from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        window_size = len(s1)
        perm1 = Counter(s1)
        perm2 = Counter(s2[:window_size])

        if perm1 == perm2:
            return True

        for i in range(window_size, len(s2)):
            perm2[s2[i]] += 1
            perm2[s2[i - window_size]] -= 1
            if perm2 == perm1:
                return True

        return False