# Last updated: 8/4/2025, 10:46:38 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            pivot = nums[mid]
            if target == pivot:
                return mid
            elif target < pivot:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1