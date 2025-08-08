# Last updated: 8/8/2025, 1:47:13 AM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums)-1
        p = len(nums) - 1
        res = [0] * len(nums)
        while i <= j:
            i_square, j_square = nums[i]**2, nums[j]**2
            print(f"i: {i}, {i_square}; j: {j}, {j_square}")
            if i_square < j_square:
                res[p] = j_square
                j -= 1
            else:
                res[p] = i_square
                i +=1
            p -= 1

        return res