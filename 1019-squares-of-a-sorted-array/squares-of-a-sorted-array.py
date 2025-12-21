class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if nums[0] >= 0: return [i ** 2 for i in nums]
        elif nums[-1] <= 0: return [i ** 2 for i in nums][::-1]

        res = [0] * len(nums)
        left = 0
        right = len(nums) - 1

        # for i in range(len(nums), -1, -1):
        for pointer in range(len(nums) - 1, -1, -1):
            if abs(nums[right]) >= abs(nums[left]):
                res[pointer] = nums[right] ** 2
                right -= 1
            else:
                res[pointer] = nums[left] ** 2
                left += 1

        return res