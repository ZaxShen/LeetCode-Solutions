class Solution:
    # O(n), O(n)
    def isValid(self, s: str) -> bool:
        mapping = {"{": "}", "[": "]", "(": ")"}
        stack = []

        for i in s:
            if i in mapping:
                stack.append(i)
            elif not stack or mapping.get(stack.pop()) != i:
                    return False

        return len(stack) == 0
