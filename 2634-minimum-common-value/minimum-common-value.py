class Solution:
	# O(m + n), O(m)
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        intersection = set(nums1) & set(nums2)
        if intersection:
            return min(intersection)
        return -1