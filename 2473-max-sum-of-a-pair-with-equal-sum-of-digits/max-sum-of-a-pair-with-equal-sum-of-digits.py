from collections import defaultdict

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def helper(num: int) -> int:
            res = 0
            while num != 0:
                res += num % 10
                num = num // 10
            
            return res

        res = -1
        hashmap = defaultdict(int)

        for i in nums:
            digit = helper(i)
            if digit in hashmap:
                res = max(res, i + hashmap[digit])
            hashmap[digit] = max(hashmap[digit], i)

        return res

