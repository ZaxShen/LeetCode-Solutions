class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for i in s:
            if i in mapping:
                stack.append(i)
            else:
                if stack and mapping.get(stack[-1]) == i:
                    stack.pop()
                # Early stopping
                else:
                    return False

        return len(stack) == 0