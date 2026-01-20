class Solution:
    # O(n+m), O(n+m)
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []

        def helper(s: str) -> list:
            stack = []
            for i in s:
                if stack and i == '#':
                    stack.pop()
                elif i != '#':
                    stack.append(i)

            return stack

        return helper(s) == helper(t)
