class Solution:
    # O(m + n), O(1)
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # Early Termination: check if there is an overlap
        if nums1[-1] < nums2[0] or nums2[-1] < nums1[0]:
            return -1
        
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            num1, num2 = nums1[i], nums2[j]
            if num1 == num2:
                return num1
            elif num1 < num2:
                i += 1
            else:
                j += 1

        return -1