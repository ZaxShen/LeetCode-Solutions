class Solution:
    # O(n), O(n)
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        desc_stack = []

        for i in nums2:
            while desc_stack and desc_stack[-1] < i:
                prev_greatest = desc_stack.pop()
                hashmap[prev_greatest] = i
            desc_stack.append(i)

        res = [-1] * len(nums1)

        for idx, i in enumerate(nums1):
            if i in hashmap:
                res[idx] = hashmap[i]
        
        return res