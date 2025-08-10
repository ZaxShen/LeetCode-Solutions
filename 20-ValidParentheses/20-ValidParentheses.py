# Last updated: 8/9/2025, 11:22:38 PM
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