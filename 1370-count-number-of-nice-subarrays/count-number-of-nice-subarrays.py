from collections import defaultdict

class Solution:
    # O(n), O(n)
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        seen[0] = 1
        res = prefix = 0

        for num in nums:
            prefix += num % 2
            target = prefix - k

            if target in seen:
                res += seen[target]

            seen[prefix] += 1

        return res
