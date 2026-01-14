class Solution:
    # O(n), O(1)
    def maximumSum(self, nums: List[int]) -> int:
        # O(n), O(1)
        def helper(num: int) -> str:
            res = 0
            while num != 0:
                res += num % 10
                num = num // 10

            return res + num

        d = dict()
        res = -float('inf')
        
        for i in nums:
            digits = helper(i)
            if digits in d:
                res = max(res, d[digits] + i)
                d[digits] = max(d[digits], i)
            else:
                d[digits] = i

        return res if res != -float('inf') else -1