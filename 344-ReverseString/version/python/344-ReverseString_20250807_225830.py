# Last updated: 8/7/2025, 10:58:30 PM
# O(n), O(1)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(i, j):
            if i < j:
                s[i], s[j] = s[j], s[i]
                helper(i+1, j-1)
        helper(0, len(s)-1)
        