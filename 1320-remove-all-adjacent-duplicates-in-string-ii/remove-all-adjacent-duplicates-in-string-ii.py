class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # [char, count]

        for i in s:
            if stack and stack[-1][0] == i:
                stack[-1][1] += 1
                if stack [-1][1] == k:
                    del stack[-1]
            else:
                stack.append([i, 1])

        res = []

        for k, v in stack:
            res.append(k * v)

        return ''.join(res)