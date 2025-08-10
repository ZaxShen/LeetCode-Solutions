# Last updated: 8/9/2025, 11:02:44 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = [i.lower() for i in s if i.isalnum()]
        return res == res[::-1]
