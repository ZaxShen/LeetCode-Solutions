class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        ds = []
        res = [-1] * len(nums1)

        for v in nums2:
            while ds and ds[-1] < v:
                last_greatest = ds.pop()
                hashmap[last_greatest] = v
            ds.append(v)

        for i, v in enumerate(nums1):
            if v in hashmap:
                res[i] = hashmap[v]

        return res
