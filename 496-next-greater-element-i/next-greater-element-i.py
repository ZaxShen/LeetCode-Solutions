class Solution:
    # O(n), O(n)
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = {}

        asc_stack = []
        
        for i in nums2:
            while asc_stack and asc_stack[-1] < i:
                mapping[asc_stack.pop()] = i
            asc_stack.append(i)

        res = [-1] * len(nums1)
        
        for idx, i in enumerate(nums1):
            if i in mapping:
                res[idx] = mapping[i]

        return res