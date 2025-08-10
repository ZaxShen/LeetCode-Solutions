# Last updated: 8/10/2025, 3:17:30 PM
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