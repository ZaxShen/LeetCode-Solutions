class Solution:
    # O(n), O(1)
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num): return '0'

        mono_stack = []

        # k < len(num)
        for i in num:
            while mono_stack and mono_stack[-1] > i and k > 0:
                mono_stack.pop()
                k -= 1
            mono_stack.append(i)

        if k > 0: mono_stack = mono_stack[:-k]
        res = ''.join(mono_stack)

        return res.lstrip('0') or '0'