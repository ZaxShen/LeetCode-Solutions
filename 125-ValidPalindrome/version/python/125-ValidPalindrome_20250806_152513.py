# Last updated: 8/6/2025, 3:25:13 PM
# O(n), O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = (''.join(i.lower() for i in s if i.isalnum()))
        return s == s[::-1]
