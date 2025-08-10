# Last updated: 8/9/2025, 10:32:34 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in d:
                return d[diff], i
            d[v] = i
        
        return (-1, -1)