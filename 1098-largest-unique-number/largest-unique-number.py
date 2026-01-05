from collections import Counter

class Solution:
    # O(n), O(k)
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = Counter(nums)

        res = -float('inf')
        for k, v in count.items():
            if v == 1:
                res = max(res, k)

        return res if res != -float('inf') else -1