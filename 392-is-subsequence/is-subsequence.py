class Solution:
    # O(n), O(1)
    def isSubsequence(self, s: str, t: str) -> bool:
        # Handle edge cases
        if len(s) > len(t):
            return False

        i = 0
        for char in t:
            # Early termination
            if i == len(s):
                return True
            if s[i] == char:
                i += 1
            
        return i == len(s)