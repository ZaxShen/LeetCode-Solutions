from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        win_size = len(s1)

        # First window
        perm1 = Counter(s1)
        perm2 = Counter(s2[:win_size])

        if perm1 == perm2:
            return True

        # Slide window
        for i in range(win_size, len(s2)):
            perm2[s2[i]] += 1
            perm2[s2[i - win_size]] -= 1
            if perm1 == perm2:
                return True

        return False
