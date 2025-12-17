class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [0] * n
        stack = [] # Monotonic decreasing stack

        # Iterate backwards
        for i in range(n - 1, -1, -1):
            count = 0
            # While the current person is taller than the person on the stack
            while stack and heights[i] > stack[-1]:
                stack.pop()
                count += 1
            
            # If the stack isn't empty, they can see the person taller than them
            if stack:
                count += 1
                
            res[i] = count
            stack.append(heights[i])
            
        return res