# Last updated: 8/10/2025, 2:52:50 PM
class Solution:
	# O(n), O(n)
    def reverseOnlyLetters(self, s: str) -> str:
        left, right = 0, len(s) - 1
        s = list(s)
        while left < right:
            if s[left].isalpha() and s[right].isalpha():
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            if s[left].isalpha() == False:
                left += 1
            if s[right].isalpha() == False:
                right -= 1

        return "".join(s)