class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(sentence: str) -> str:
            stack = []
            for char in sentence:
                if char != '#':
                    stack.append(char)
                elif stack:
                    stack.pop()

            return ''.join(stack)

        return helper(s) == helper(t)