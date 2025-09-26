class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(sentence: str) -> str:
            stack = []
            for char in sentence:
                if char == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)

            return stack

        return helper(s) == helper(t)