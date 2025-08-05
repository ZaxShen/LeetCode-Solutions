# Last updated: 8/4/2025, 10:43:32 PM
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for i in s:
            if i == '*':
                stack.pop()
            else:
                stack.append(i)

        return ''.join(stack)