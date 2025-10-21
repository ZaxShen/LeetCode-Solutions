class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(s: str) -> str:
            stack = []
            for char in s:
                if char != '#':
                    stack.append(char)
                else:
                    if stack:
                        stack.pop()

            return stack

        return helper(s) == helper(t)
