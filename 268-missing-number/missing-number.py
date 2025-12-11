class Solution:
    # O(n), O(1)
    def missingNumber(self, nums: List[int]) -> int:
        all_nums = range(len(nums) + 1)
        hashset = set(nums)

        for i in all_nums:
            if i not in hashset:
                return i