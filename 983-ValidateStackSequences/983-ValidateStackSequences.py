# Last updated: 8/4/2025, 10:46:29 PM
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0

        for i in pushed:
            stack.append(i)
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        return not stack
