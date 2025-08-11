# Last updated: 8/10/2025, 9:23:58 PM
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix_sum = []
        curr = 0
        for num in nums:
            curr += num
            prefix_sum.append(curr)

        return prefix_sum