# Last updated: 8/4/2025, 10:43:28 PM
class Solution:
    # O(n+m), O(1)
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        i1 = i2 = 0
        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] == nums2[i2]:
                return nums1[i1]
            elif nums1[i1] > nums2[i2]:
                i2 += 1
            else:
                i1 += 1

        return -1