class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        si = ti = res = 0

        while si < len(s) and ti < len(t):
            if s[si] == t[ti]:
                res += 1
                si += 1
            ti += 1
            # Early termination
            if res == len(s):
                return True

        return res == len(s)