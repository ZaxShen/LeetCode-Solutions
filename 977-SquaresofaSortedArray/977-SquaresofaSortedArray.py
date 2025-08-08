# Last updated: 8/8/2025, 1:49:03 AM
class Solution:
    # O(n), O(1)
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums)-1
        p = len(nums) - 1
        res = [0] * len(nums)
        while i <= j:
            i_square, j_square = nums[i]**2, nums[j]**2
            if i_square < j_square:
                res[p] = j_square
                j -= 1
            else:
                res[p] = i_square
                i +=1
            p -= 1

        return res