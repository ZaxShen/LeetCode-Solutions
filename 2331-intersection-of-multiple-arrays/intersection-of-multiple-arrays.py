class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        hashset = set(nums[0])
        
        for i in nums[1:]:
            hashset &= set(i)

        return sorted(hashset)