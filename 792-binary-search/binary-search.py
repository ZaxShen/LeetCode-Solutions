class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binarySearch(left, right):
            if left > right:
                return -1

            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                return binarySearch(left, mid - 1)

            else:
                return binarySearch(mid + 1, right)

        return binarySearch(0, len(nums) - 1)