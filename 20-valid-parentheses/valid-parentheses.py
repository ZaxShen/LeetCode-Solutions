class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for i in s:
            if stack and mapping.get(stack[-1]) == i:
                stack.pop()
            else:
                stack.append(i)

        return len(stack) == 0