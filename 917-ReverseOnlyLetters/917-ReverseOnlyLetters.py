# Last updated: 8/12/2025, 7:11:03 PM
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            if not l[left].isalpha():
                left += 1
            elif not l[right].isalpha():
                right -= 1
            else:
                l[left], l[right] = l[right], l[left]
                left += 1
                right -= 1

        return ''.join(l)