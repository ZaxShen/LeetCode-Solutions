class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Early Termination
        if len(s) > len(t) or set(s) > set(t):
            return False

        si = ti = 0
        while si < len(s) and ti < len(t):
            if s[si] == t[ti]:
                si += 1
            # Early Termination
            if len(s) - si > len(t) - ti:
                return False
            ti += 1

        return len(s) == si