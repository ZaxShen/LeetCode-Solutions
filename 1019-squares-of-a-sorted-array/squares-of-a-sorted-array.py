class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if nums[0] >= 0:
            return [num ** 2 for num in nums]
        elif nums[-1] <= 0:
            return list(reversed([num ** 2 for num in nums]))

        res = [0] * len(nums)
        left, right = 0, len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            abs_left, abs_right = abs(nums[left]), abs(nums[right])
            if abs_left < abs_right:
                res[i] = abs_right ** 2
                right -= 1
            else:
                res[i] = abs_left ** 2
                left += 1

        return res

