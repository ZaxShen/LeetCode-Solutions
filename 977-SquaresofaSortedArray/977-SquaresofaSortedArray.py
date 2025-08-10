# Last updated: 8/9/2025, 10:43:37 PM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1

        # For Full non-positive number
        if nums[i] >= 0:
            return [num ** 2 for num in nums]
        elif nums[j] <= 0:
            return [num ** 2 for num in nums][::-1]


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
