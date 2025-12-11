class Solution:
    # O(n), O(n)
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mono_stack = []
        mapping = {}

        for i in nums2:
            while mono_stack and mono_stack[-1] < i:
                mapping[mono_stack.pop()] = i
            mono_stack.append(i)

        res = [-1] * len(nums1)

        for idx, i in enumerate(nums1):
            if i in mapping:
                res[idx] = mapping[i]

        return res
