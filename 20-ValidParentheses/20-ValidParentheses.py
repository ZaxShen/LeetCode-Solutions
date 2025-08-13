# Last updated: 8/12/2025, 8:00:38 PM
class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'(': ')', '{': '}', '[': ']'}
        stack = []

        for char in s:
            if stack and mapping.get(stack[-1]) == char:
                stack.pop()
            else:
                stack.append(char)

        return len(stack) == 0