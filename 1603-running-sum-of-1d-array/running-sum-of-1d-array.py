class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        prefix = 0
        for num in nums:
            prefix += num
            res.append(prefix)

        return res