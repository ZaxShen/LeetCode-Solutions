# Last updated: 8/4/2025, 10:45:08 PM
class Solution:
    # O(n), O(n)
    def runningSum(self, nums: list[int]) -> list[int]:
        result = []
        acc = 0
        
        for i in range(len(nums)):
            acc += nums[i]
            result.append(acc)
            
        return result