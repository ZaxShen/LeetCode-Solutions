# Last updated: 8/11/2025, 5:32:29 PM
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = 0

        while i < len(nums1) and j < len(nums2):
            n1, n2 = nums1[i], nums2[j]
            if n1 == n2:
                return n1
            elif n1 < n2:
                i += 1
            else:
                j += 1

        return -1