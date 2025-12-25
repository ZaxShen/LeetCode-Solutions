class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        mins = [0] * len(arr)
        asc_stack = []

        for idx, i in enumerate(arr):
            while asc_stack and arr[asc_stack[-1]] > i:
                asc_stack.pop()
            
            if asc_stack:
                prev_sum = mins[asc_stack[-1]]
                mins[idx] = prev_sum + i * (idx - asc_stack[-1])
            else:
                mins[idx] = i * (idx + 1)
            
            asc_stack.append(idx)

        return sum(mins) % MOD
            