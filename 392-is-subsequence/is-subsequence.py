class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Handle edge cases
        if len(s) > len(t):
            return False

        i, j = 0, 0
        for j in range(len(t)):
            if i < len(s) and s[i] == t[j]:
                i += 1
            
        return i == len(s)