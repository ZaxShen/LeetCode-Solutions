# Last updated: 8/4/2025, 10:46:22 PM
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            if stack and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)

        return "".join(stack)
