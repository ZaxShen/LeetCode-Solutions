class Solution:
    # O(n), O(1)
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        prefix = 0

        for idx, i in enumerate(nums):
            if prefix == total - prefix - i:
                return idx
            prefix += i

        return -1