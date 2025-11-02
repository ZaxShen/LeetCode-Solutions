class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # Edge Case: If k >= length, remove all digits
        if k >= len(num): return '0'

        mono_stack = []

        for i in num:
            while k > 0 and mono_stack and mono_stack[-1] > i:
                mono_stack.pop()
                k -= 1
            mono_stack.append(i)

        # Edge Case: Remove remaining k digits from end
        if k > 0: mono_stack = mono_stack[:-k]

        # Edge Case: Handle leading zeros and empty result
        res = ''.join(mono_stack).lstrip('0') or '0'
        
        return res