class Solution:
    # O(m+n), O(n)
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = {}
        desc_stack = []

        # Record the next greater element in mapping
        for i in nums2:
            while desc_stack and desc_stack[-1] < i:
                mapping[desc_stack.pop()] = i
            desc_stack.append(i)

        res = [-1] * len(nums1)
        for idx, i in enumerate(nums1):
            if i in mapping:
                res[idx] = mapping[i]

        return res