class Solution:
    # O(n), O(1)
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)

        left, right = 0, len(s) - 1
        while left <= right:
            if s[left].isalpha() == False:
                left += 1
            elif s[right].isalpha() == False:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return "".join(s)