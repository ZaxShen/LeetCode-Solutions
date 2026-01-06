class Solution:
    # O(n), O(k)
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # Store [char, freq]

        for i in s:
            if stack and stack[-1][0] == i:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()       
            else:
                stack.append([i, 1])

        res = ''.join(char * freq for char, freq in stack)

        return res