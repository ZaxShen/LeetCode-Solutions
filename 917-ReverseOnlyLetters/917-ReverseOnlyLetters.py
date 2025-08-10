# Last updated: 8/10/2025, 2:52:57 PM
class Solution:
    # O(n), O(n)
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        i, j = 0, len(s) - 1
        while i <= j:
            if s[i].isalpha() and s[j].isalpha():
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            else:
                if not s[i].isalpha():
                    i += 1
                if not s[j].isalpha():
                    j -= 1
        
        return ''.join(s)