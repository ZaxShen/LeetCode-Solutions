from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        seen[0] = 1
        prefix = res = 0

        for idx, i in enumerate(nums):
            prefix += i
            lookup = prefix % k

            if lookup in seen:
                res += seen[lookup]
            
            seen[lookup] += 1

        print(seen)
        return res
