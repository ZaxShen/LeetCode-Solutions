class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        asc_stack = []

        for i in num:
            while k > 0 and asc_stack and asc_stack[-1] > i:
                asc_stack.pop()
                k -= 1
            asc_stack.append(i)

        if k > 0:
            asc_stack = asc_stack[:-k]
        
        res = ''.join(asc_stack).lstrip('0')

        return res or '0'
