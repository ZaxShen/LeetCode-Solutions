class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        hashset = set(nums[0])

        for arr in nums:
            hashset &= set(arr)

        return sorted(hashset)
