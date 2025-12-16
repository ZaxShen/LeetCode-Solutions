class Solution:
    # O(n), O(1)
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        seen = {0: 1}
        prefix = res = 0

        for i in nums:
            prefix += i
            lookup = prefix % k

            if lookup in seen:
                res += seen[lookup]
                seen[lookup] += 1
            else:
                seen[lookup] = 1

        return res
