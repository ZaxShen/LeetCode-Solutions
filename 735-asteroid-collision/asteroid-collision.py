class Solution:
    # O(n), O(n)
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in asteroids:
            # ? >
            if i > 0:
                stack.append(i)
            else:
                # > <<
                while stack and stack[-1] > 0 and stack[-1] + i < 0:
                    stack.pop()
                # > <
                if stack and stack[-1] + i == 0:
                    stack.pop()
                # >> <
                elif stack and stack[-1] + i > 0:
                    continue
                # []
                else:
                    stack.append(i)

        return stack