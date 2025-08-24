class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        prefix = 0

        for i, num in enumerate(nums):
            prefix += num
            if prefix - num == total - prefix:
                return i

        return -1