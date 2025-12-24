class Solution:
    # O(n), O(k)
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        seen = {0: 1}
        prefix = res = 0

        # 4,5,0,-2,-3,1
        # 4, 9, 9, 7, 4, 5
        # 4, 4, 4, 2, 4, 0

        for i in nums:
            prefix += i
            lookup = prefix % k

            if lookup in seen:
                res += seen[lookup]
                seen[lookup] += 1
            else:
                seen[lookup] = 1

        return res
