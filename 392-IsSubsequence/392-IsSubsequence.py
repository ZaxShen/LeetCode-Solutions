# Last updated: 8/18/2025, 9:15:13 AM
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Handle edge cases
        if len(s) > len(t):
            return False

        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return len(s) == i