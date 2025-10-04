class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        
        i = 0
        for j in range(len(t)):
            if len(s) == i:
                return True
            if s[i] == t[j]:
                i += 1

        return i == len(s)


