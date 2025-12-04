class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k: return '0'

        mono_stack = []

        for i in num:
            while k != 0 and mono_stack and mono_stack[-1] > i:
                mono_stack.pop()
                k -= 1
            mono_stack.append(i)

        if k > 0: mono_stack = mono_stack[:-k] 

        return ''.join(mono_stack).lstrip('0') or '0'