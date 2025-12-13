class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for i in s:
            if stack and mapping.get(stack[-1]) == i:
                stack.pop()
            else:
                # Early Termination
                if i in mapping.values():
                    return False
                stack.append(i)
        
        return len(stack) == 0