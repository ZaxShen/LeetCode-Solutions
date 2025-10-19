class Solution:
    # O(m + n), O(1)
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        intersection = set(nums1) & set(nums2)

        if intersection:
            return min(intersection)
        return -1