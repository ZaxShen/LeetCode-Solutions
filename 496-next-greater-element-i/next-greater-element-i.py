from collections import defaultdict

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = defaultdict(int)
        mono_stack = []

        for idx, i in enumerate(nums2):
            while mono_stack and mono_stack[-1] < i:
                hashmap[mono_stack.pop()] = i
            mono_stack.append(i)

        res = []
        for i in nums1:
            if i in hashmap:
                res.append(hashmap[i])
            else:
                res.append(-1)

        return res
