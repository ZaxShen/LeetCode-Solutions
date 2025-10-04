class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        
        si = ti = 0
        while si < len(s) and ti < len(t):
            if s[si] == t[ti]:
                si += 1
            ti += 1

        return len(s) == si

