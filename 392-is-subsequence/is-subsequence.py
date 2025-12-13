class Solution:
    # O(n), O(n)
    def isSubsequence(self, s: str, t: str) -> bool:
        # Early Termination
        if len(s) > len(t) or set(s) > set(t):
            return False

        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            # Early Termination
            if len(s) - i > len(t) - j:
                return False
            j += 1

        return i == len(s)