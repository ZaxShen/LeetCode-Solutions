class Solution:
    # O(n), O(1)
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                # print(nums, left)
                # print(nums[left], nums[right])
                nums[left], nums[right] = nums[right], nums[left]
                # print(nums, left)
                # print('-'*20)
                left += 1

        # 0, 1, 0, 3, 12 0, 0
        # 1, 0, 0 ,3, 12 0, 1
        # 1, 3, 0, 0, 12 0, 3