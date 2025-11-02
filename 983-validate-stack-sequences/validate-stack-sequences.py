class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # Edge Case
        if len(pushed) != len(popped): return False

        stack = []
        i = j = 0

        while i < len(pushed):
            stack.append(pushed[i])
            i += 1
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        return not stack
