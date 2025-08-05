# Last updated: 8/4/2025, 10:46:36 PM
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(s):
            stack = []
            for i in s:
                if i != "#":
                    stack.append(i)
                elif stack:
                    stack.pop()

            return stack

        return build(s) == build(t)