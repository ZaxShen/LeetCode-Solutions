# Last updated: 8/11/2025, 6:17:11 PM
class Solution:
    # O(n), O(1)
    def reversePrefix(self, word: str, ch: str) -> str:
        def helper(s: str) -> str:
            l = list(s)
            left, right = 0, len(s) - 1
            while left < right:
                l[left], l[right] = l[right], l[left]
                left += 1
                right -= 1

            return ''.join(l)

        for i in range(len(word)):
            if word[i] == ch:
                index = i + 1
                res = helper(word[:index]) + word[index:]
                return res

        return word