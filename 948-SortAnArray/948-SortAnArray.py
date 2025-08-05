# Last updated: 8/4/2025, 10:46:33 PM
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums) - 1)
        return nums
    
    # O(n log(n)), O(log(n))
    def quicksort(self, arr, start, end):
        if start > end: return
        
        l, r = start, end
        pivot = arr[(l + r) // 2]
        
        while l <= r:
            while l <= r and arr[l] < pivot: l += 1
            while l <= r and pivot < arr[r]: r -= 1
            
            if l <= r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
            
        self.quicksort(arr, start, r)
        self.quicksort(arr, l, end)