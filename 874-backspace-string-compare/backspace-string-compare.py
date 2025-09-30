class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(input: str) -> str:
            stack = []
            for char in input:
                if char != '#':
                    stack.append(char)
                else:
                    if stack:
                        stack.pop()
            
            return ''.join(stack)

        return helper(s) == helper(t)