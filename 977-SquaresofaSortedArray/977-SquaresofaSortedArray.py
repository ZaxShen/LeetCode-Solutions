# Last updated: 8/9/2025, 10:49:34 PM
class Solution:
    # O(n), O(1)
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        p = len(nums) - 1
        res = [0] * len(nums)

        while i <= j:
            i_sq, j_sq = nums[i] ** 2, nums[j] ** 2
            if i_sq < j_sq:
                res[p] = j_sq
                j -= 1
            else:
                res[p] = i_sq
                i += 1
            p -= 1

        return res