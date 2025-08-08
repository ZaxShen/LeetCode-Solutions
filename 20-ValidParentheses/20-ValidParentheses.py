# Last updated: 8/8/2025, 11:43:57 AM
class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'(': ')', '{': '}', '[': ']'}
        stack = []

        for char in s:
            if stack and mapping.get(stack[-1]) == char:
                stack.pop()
            else:
                stack.append(char)
        
        return stack == []
            