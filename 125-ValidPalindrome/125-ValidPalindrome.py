# Last updated: 8/7/2025, 11:14:00 PM
class Solution:
    # O(n), O(n)
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(i.lower() for i in s if i.isalnum())
        return s == s[::-1]