class Solution:
    # O(n), O(n)
    def isValid(self, s: str) -> bool:
        mapping = {"{": "}", "[": "]", "(": ")"}
        stack = []

        for char in s:
            if char in mapping:
                stack.append(char)
            else:
                if not stack:
                    return False
                prev_char = stack.pop()
                if mapping[prev_char] != char:
                    return False

        return len(stack) == 0