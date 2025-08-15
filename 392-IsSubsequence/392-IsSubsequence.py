# Last updated: 8/15/2025, 5:28:40 PM
class Solution:
    # O(n), O(1)
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)