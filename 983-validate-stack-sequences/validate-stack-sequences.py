class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # Edge Case
        if len(pushed) != len(popped): return False

        stack = []
        j = 0

        for i in pushed:
            stack.append(i)
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        return not stack

        
