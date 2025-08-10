# Last updated: 8/9/2025, 10:40:56 PM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        pos = len(nums) - 1
        res = [0] * len(nums)

        while i <= j:
            i_sqr, j_sqr = nums[i] ** 2, nums[j] ** 2
            if i_sqr < j_sqr:
                res[pos] = j_sqr
                j -= 1
            else:
                res[pos] = i_sqr
                i += 1
            pos -= 1
        
        return res
