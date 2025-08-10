# Last updated: 8/9/2025, 10:51:16 PM
class Solution:
	# O(n), O(1)
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1

		# Edge Cases Handling
        if nums[i] >= 0:
            return [num ** 2 for num in nums]
        elif nums[j] <= 0:
            return [num ** 2 for num in nums][::-1]

        pos = len(nums) - 1
        res = [0] * len(nums)
        
        while i <= j:
            i_sq, j_sq = nums[i] ** 2, nums[j] ** 2
            if i_sq < j_sq:
                res[pos] = j_sq
                j -= 1
            else:
                res[pos] = i_sq
                i += 1
            pos -= 1
        
        return res