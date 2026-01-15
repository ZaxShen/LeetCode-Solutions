class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # Edge case
        if k == len(num): return "0"

        stack = []

        for i in num:
            while k > 0 and stack and stack[-1] > i:
                stack.pop()
                k -= 1
            stack.append(i)

        res = ''.join(stack).lstrip('0')
        if k > 0:
            res = res[:-k]

        return res or '0'