class Solution:
    # O(n), O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for idx, i in enumerate(nums):
            diff = target - i
            if diff in hashmap:
                return [hashmap[diff], idx]
            hashmap[i] = idx
            
        return [-1, -1]