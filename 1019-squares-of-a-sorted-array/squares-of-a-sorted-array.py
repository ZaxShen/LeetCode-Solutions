class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1

        # Handle edge cases
        if nums[left] >= 0:
            return [num ** 2 for num in nums]
        elif nums[right] <= 0:
            return [num ** 2 for num in nums][::-1]


        res = [0] * len(nums)
        pointer = len(nums) - 1


        while left <= right:
            abs_left, abs_right = abs(nums[left]), abs(nums[right])
            if abs_left < abs_right:
                res[pointer] = abs_right ** 2
                right -= 1
            else:
                res[pointer] = abs_left ** 2
                left += 1
            pointer -= 1

        return res
