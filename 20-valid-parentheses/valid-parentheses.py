class Solution:
    # O(n), O(1)
    def isValid(self, s: str) -> bool:
        mapping = {"{": "}", "[": "]", "(": ")"}
        stack = []

        for i in s:
            if i in mapping:
                stack.append(i)
            elif not stack or mapping[stack.pop()] != i:
                return False

        return len(stack) == 0